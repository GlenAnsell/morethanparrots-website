"""
Microsoft Graph API email sender for Django.
Supports both client-credentials (application) and delegated flows.

For shared mailboxes, client-credentials is recommended:
1. Azure App Registration -> API Permissions -> Add Mail.Send (Application)
2. Grant admin consent
3. Set MS_GRAPH_SENDER_UPN to the shared mailbox email

For delegated (existing token), the app reads ~/.hermes/auth/office365/ tokens.
"""

import json
import os
import time
import requests
from django.conf import settings


TOKEN_CACHE = {"access_token": None, "expires_at": 0}


def _get_client_credentials_token():
    """OAuth2 client credentials flow for application permissions."""
    tenant_id = getattr(settings, "MS_GRAPH_TENANT_ID", "")
    client_id = getattr(settings, "MS_GRAPH_CLIENT_ID", "")
    client_secret = getattr(settings, "MS_GRAPH_CLIENT_SECRET", "")

    if not all([tenant_id, client_id, client_secret]):
        raise RuntimeError("MS_GRAPH_TENANT_ID, CLIENT_ID, CLIENT_SECRET required")

    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://graph.microsoft.com/.default",
    }
    resp = requests.post(url, data=data, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data["access_token"], time.time() + data.get("expires_in", 3600)


def _get_delegated_token(account_name):
    """Read cached delegated token and refresh if needed."""
    # Try absolute path first (production), then expanduser
    token_path = os.path.expanduser(f"~/.hermes/auth/office365/{account_name}.json")
    if not os.path.exists(token_path):
        # Fallback for systemd services that may have different HOME
        alt_path = f"/var/www/.hermes/auth/office365/{account_name}.json"
        if os.path.exists(alt_path):
            token_path = alt_path
        else:
            raise RuntimeError(f"No delegated token found at {token_path}")

    with open(token_path, "r") as f:
        tok = json.load(f)

    # expires_at may be in milliseconds (JS timestamps) or seconds
    expires_at = tok.get("expires_at", 0)
    if expires_at > 10**12:
        expires_at = expires_at / 1000.0

    # Check expiry with 5-min buffer
    if expires_at > time.time() + 300:
        return tok["access_token"]

    # Refresh
    tenant_id = getattr(settings, "MS_GRAPH_TENANT_ID", "")
    client_id = getattr(settings, "MS_GRAPH_CLIENT_ID", "")
    refresh_token = tok.get("refresh_token", "")

    if not all([tenant_id, client_id, refresh_token]):
        raise RuntimeError("Cannot refresh: missing tenant_id, client_id, or refresh_token")

    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "refresh_token": refresh_token,
        "scope": "https://graph.microsoft.com/Mail.Send https://graph.microsoft.com/User.Read offline_access",
    }
    resp = requests.post(url, data=data, timeout=30)
    resp.raise_for_status()
    new_tok = resp.json()

    # Update cache file
    tok["access_token"] = new_tok["access_token"]
    tok["refresh_token"] = new_tok.get("refresh_token", tok.get("refresh_token", ""))
    tok["expires_at"] = int((time.time() + new_tok.get("expires_in", 3600)) * 1000)
    with open(token_path, "w") as f:
        json.dump(tok, f)
    os.chmod(token_path, 0o600)

    return tok["access_token"]


def _get_token():
    """Return a valid Graph access token, preferring cached."""
    # Use client credentials if configured
    if getattr(settings, "MS_GRAPH_CLIENT_SECRET", ""):
        if TOKEN_CACHE["access_token"] and TOKEN_CACHE["expires_at"] > time.time() + 300:
            return TOKEN_CACHE["access_token"]
        token, expires = _get_client_credentials_token()
        TOKEN_CACHE["access_token"] = token
        TOKEN_CACHE["expires_at"] = expires
        return token

    # Fallback to delegated token
    account = getattr(settings, "MS_GRAPH_DELEGATED_ACCOUNT", "xcode")
    return _get_delegated_token(account)


def send_email(to_email, subject, html_body, text_body="", from_email=None):
    """
    Send email via Microsoft Graph API.

    Args:
        to_email: recipient address
        subject: email subject
        html_body: HTML content
        text_body: plain text fallback (optional)
        from_email: sender UPN (defaults to MS_GRAPH_SENDER_UPN or DEFAULT_FROM_EMAIL)

    Returns:
        (success: bool, error_or_response: str)
    """
    try:
        token = _get_token()
    except Exception as e:
        return False, f"Token error: {e}"

    sender = from_email or getattr(settings, "MS_GRAPH_SENDER_UPN", "") or getattr(settings, "DEFAULT_FROM_EMAIL", "")
    if "<" in sender:
        # Extract email from "Name <email>" format
        sender = sender.split("<")[1].split(">")[0].strip()

    if not sender:
        return False, "No sender configured (MS_GRAPH_SENDER_UPN or DEFAULT_FROM_EMAIL)"

    url = f"https://graph.microsoft.com/v1.0/users/{sender}/sendMail"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    message = {
        "subject": subject,
        "body": {"contentType": "HTML", "content": html_body},
        "toRecipients": [{"emailAddress": {"address": to_email}}],
    }

    # If text_body provided, include it as a comment or note — Graph v1.0 doesn't
    # support multipart/alternative directly, so we stick with HTML primary.
    # The recipient's client will render the HTML.

    payload = {"message": message, "saveToSentItems": "true"}

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        if resp.status_code in (200, 202):
            return True, "Sent"
        return False, f"Graph API error {resp.status_code}: {resp.text[:500]}"
    except requests.RequestException as e:
        return False, f"Request error: {e}"

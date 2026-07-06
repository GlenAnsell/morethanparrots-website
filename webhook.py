#!/usr/bin/env python3
import os
import sys
import hmac
import hashlib
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler

SECRET = os.environ.get('WEBHOOK_SECRET', '')
DEPLOY_SCRIPT = '/var/www/mtp/deploy.sh'
LOG_FILE = '/var/log/mtp-webhook.log'

def verify_signature(payload, signature):
    if not SECRET:
        return True  # No secret configured, skip verification
    if not signature:
        return False
    expected = 'sha256=' + hmac.new(SECRET.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)

class WebhookHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        with open(LOG_FILE, 'a') as f:
            f.write(f"{self.log_date_time_string()} - {format % args}\n")
    
    def do_POST(self):
        if self.path != '/webhook':
            self.send_error(404)
            return
        
        content_length = int(self.headers.get('Content-Length', 0))
        payload = self.rfile.read(content_length)
        signature = self.headers.get('X-Hub-Signature-256', '')
        
        if not verify_signature(payload, signature):
            self.send_error(401, 'Invalid signature')
            return
        
        event = self.headers.get('X-GitHub-Event', '')
        if event != 'push':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Event ignored')
            return
        
        # Run deploy script
        try:
            result = subprocess.run([DEPLOY_SCRIPT], capture_output=True, text=True, timeout=120)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"Deploy triggered\n\n{result.stdout}\n{result.stderr}".encode())
        except Exception as e:
            self.send_error(500, str(e))
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'MTP Webhook Receiver')

if __name__ == '__main__':
    port = int(os.environ.get('WEBHOOK_PORT', '9000'))
    server = HTTPServer(('127.0.0.1', port), WebhookHandler)
    print(f'Webhook server running on port {port}')
    server.serve_forever()

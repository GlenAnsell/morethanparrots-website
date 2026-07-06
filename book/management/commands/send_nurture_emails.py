"""
Django management command: send_nurture_emails

Sends Day 2, Day 7, and Day 14 nurture emails to newsletter subscribers.
Run via cron every 4 hours:
    0 */4 * * * cd /var/www/mtp && venv/bin/python manage.py send_nurture_emails

Rules:
- Day 2: sent ~48h after signup, if not already sent and not unsubscribed
- Day 7: sent ~7d after signup, if Day 2 sent and Day 7 not sent
- Day 14: sent ~14d after signup, if Day 7 sent and Day 14 not sent
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from book.models import NewsletterSubscriber
from book.email_sender import send_email


EMAILS = {
    "day_2": {
        "subject": "Why I wrote this book (and why you might care)",
        "html": """<!DOCTYPE html>
<html><body style="font-family:Inter,sans-serif;color:#1A1A2E;background:#FAFAF8;padding:40px 20px;">
<div style="max-width:560px;margin:0 auto;background:#fff;border-radius:12px;padding:40px;box-shadow:0 4px 20px rgba(26,35,78,0.08);">
  <h2 style="color:#1A234E;font-family:'Playfair Display',serif;margin-top:0;">Why I wrote this book</h2>
  <p>Hi {name},</p>
  <p>Twelve years ago, I built my first machine learning model for a client. They were a mid-sized retailer trying to predict demand. The model worked — sort of. It was about 70% accurate. They were thrilled.</p>
  <p>But here's what stuck with me: they didn't understand what the model was actually doing. They thought it was "magic." They made decisions based on its output that the data couldn't support. And when the model eventually failed — because all models fail — they had no framework for understanding why.</p>
  <p>That's the pattern I've seen repeated a hundred times since.</p>
  <p><strong>AI isn't the problem. The hype is.</strong></p>
  <p>Business owners are being sold solutions to problems they don't have, by vendors who don't understand the limitations, with expectations set by science fiction rather than engineering reality.</p>
  <p>I wrote <em>More Than Parrots, Less Than Gods</em> because I was tired of watching smart people make expensive mistakes based on bad information. This book is the guide I wish I'd had when I started — and the guide I give to every client before we talk about tools.</p>
  <p>It's skeptical without being cynical. Practical without being patronizing. And opinionated — because pretending to be neutral when the stakes are this high is itself a kind of dishonesty.</p>
  <p>If that sounds like your kind of read, <a href="https://morethanparrots.com/book/" style="color:#B87A4A;">here's where to pre-order</a>.</p>
  <p style="color:#6B7280;font-size:14px;margin-top:30px;">— Glen Ansell</p>
  <hr style="border:none;border-top:1px solid #e5e7eb;margin:30px 0;">
  <p style="font-size:12px;color:#9CA3AF;">You're receiving this because you subscribed at morethanparrots.com. <a href="https://morethanparrots.com/" style="color:#9CA3AF;">Unsubscribe</a> any time.</p>
</div>
</body></html>""",
    },
    "day_7": {
        "subject": "The one thing nobody tells you about AI",
        "html": """<!DOCTYPE html>
<html><body style="font-family:Inter,sans-serif;color:#1A1A2E;background:#FAFAF8;padding:40px 20px;">
<div style="max-width:560px;margin:0 auto;background:#fff;border-radius:12px;padding:40px;box-shadow:0 4px 20px rgba(26,35,78,0.08);">
  <h2 style="color:#1A234E;font-family:'Playfair Display',serif;margin-top:0;">The one thing nobody tells you</h2>
  <p>Hi {name},</p>
  <p>I've spent the last decade building AI systems, advising companies on AI strategy, and watching the gap between hype and reality grow wider every year.</p>
  <p>Here's the thing nobody tells you:</p>
  <p style="font-size:18px;font-weight:600;color:#1A234E;border-left:4px solid #B87A4A;padding-left:16px;margin:24px 0;">AI doesn't replace judgment. It reveals the absence of it.</p>
  <p>Companies with clear strategy, good data, and strong decision-making processes get tremendous value from AI. Companies without those things waste enormous amounts of money and time.</p>
  <p>The technology is not the differentiator. The clarity of your thinking is.</p>
  <p>That's why the first half of the book is about understanding — what AI is, what it isn't, where it works, where it fails. Only after that do we talk about implementation.</p>
  <p>Because the wrong strategy executed well is still the wrong strategy.</p>
  <p>If you haven't grabbed the book yet, <a href="https://morethanparrots.com/book/" style="color:#B87A4A;">here's the pre-order link</a>. Launch-week buyers get the AI Strategy Playbook free.</p>
  <p>In the meantime, here's something practical: <a href="https://morethanparrots.com/readiness-scorecard/" style="color:#B87A4A;">Take the AI Readiness Scorecard</a>. It'll show you exactly where your business stands — no fluff, no consultant-speak.</p>
  <p style="color:#6B7280;font-size:14px;margin-top:30px;">— Glen Ansell</p>
  <hr style="border:none;border-top:1px solid #e5e7eb;margin:30px 0;">
  <p style="font-size:12px;color:#9CA3AF;">You're receiving this because you subscribed at morethanparrots.com. <a href="https://morethanparrots.com/" style="color:#9CA3AF;">Unsubscribe</a> any time.</p>
</div>
</body></html>""",
    },
    "day_14": {
        "subject": "Ready for the full map?",
        "html": """<!DOCTYPE html>
<html><body style="font-family:Inter,sans-serif;color:#1A1A2E;background:#FAFAF8;padding:40px 20px;">
<div style="max-width:560px;margin:0 auto;background:#fff;border-radius:12px;padding:40px;box-shadow:0 4px 20px rgba(26,35,78,0.08);">
  <h2 style="color:#1A234E;font-family:'Playfair Display',serif;margin-top:0;">Ready for the full map?</h2>
  <p>Hi {name},</p>
  <p>Two weeks ago, you joined The Waiting Room. Since then you've (hopefully) seen that this isn't the usual AI hype machine.</p>
  <p>Here's what I've shared so far:</p>
  <ul>
    <li>Why the book exists — and why skepticism is a feature, not a bug</li>
    <li>The one thing nobody tells you about AI (it reveals bad judgment, it doesn't fix it)</li>
  </ul>
  <p>Now I want to make you an offer.</p>
  <p><strong>Pre-order the book before launch week</strong> and you'll get three things:</p>
  <ol>
    <li><strong>The book</strong> — all 19 chapters, ebook + paperback + hardcover formats</li>
    <li><strong>The AI Strategy Playbook</strong> — the practical companion I use with every consulting client (normally $47)</li>
    <li><strong>Launch-week Q&A access</strong> — a live session where I'll answer your specific questions</li>
  </ol>
  <p>This is the only time I'm bundling the Playbook free with the book. After launch week, it goes back to separate pricing.</p>
  <div style="text-align:center;margin:30px 0;">
    <a href="https://morethanparrots.com/book/" style="display:inline-block;background:#B87A4A;color:#fff;text-decoration:none;padding:14px 32px;border-radius:8px;font-weight:500;">Pre-Order the Book</a>
  </div>
  <p>If you're not ready yet, no pressure. The Waiting Room will keep showing up every week with honest analysis — whether you buy the book or not.</p>
  <p>But if you've been waiting for a sign that this is worth your time and money: this is it.</p>
  <p style="color:#6B7280;font-size:14px;margin-top:30px;">— Glen Ansell</p>
  <hr style="border:none;border-top:1px solid #e5e7eb;margin:30px 0;">
  <p style="font-size:12px;color:#9CA3AF;">You're receiving this because you subscribed at morethanparrots.com. <a href="https://morethanparrots.com/" style="color:#9CA3AF;">Unsubscribe</a> any time.</p>
</div>
</body></html>""",
    },
}


class Command(BaseCommand):
    help = "Send Day 2, Day 7, and Day 14 nurture emails"

    def handle(self, *args, **options):
        now = timezone.now()
        sent_count = {"day_2": 0, "day_7": 0, "day_14": 0}
        fail_count = {"day_2": 0, "day_7": 0, "day_14": 0}

        # --- Day 2: ~48h after signup ---
        day2_window_start = now - timedelta(hours=54)
        day2_window_end = now - timedelta(hours=42)
        day2_candidates = NewsletterSubscriber.objects.filter(
            is_active=True,
            nurture_unsubscribed=False,
            nurture_day_2_sent__isnull=True,
            subscribed_at__gte=day2_window_start,
            subscribed_at__lte=day2_window_end,
        )
        for sub in day2_candidates:
            name = sub.first_name or "there"
            html = EMAILS["day_2"]["html"].format(name=name)
            ok, err = send_email(sub.email, EMAILS["day_2"]["subject"], html)
            if ok:
                sub.nurture_day_2_sent = now
                sub.save(update_fields=["nurture_day_2_sent"])
                sent_count["day_2"] += 1
                self.stdout.write(self.style.SUCCESS(f"Day 2 sent to {sub.email}"))
            else:
                fail_count["day_2"] += 1
                self.stdout.write(self.style.ERROR(f"Day 2 FAILED to {sub.email}: {err}"))

        # --- Day 7: ~7d after signup, Day 2 must be sent ---
        day7_window_start = now - timedelta(days=8)
        day7_window_end = now - timedelta(days=6)
        day7_candidates = NewsletterSubscriber.objects.filter(
            is_active=True,
            nurture_unsubscribed=False,
            nurture_day_2_sent__isnull=False,
            nurture_day_7_sent__isnull=True,
            subscribed_at__gte=day7_window_start,
            subscribed_at__lte=day7_window_end,
        )
        for sub in day7_candidates:
            name = sub.first_name or "there"
            html = EMAILS["day_7"]["html"].format(name=name)
            ok, err = send_email(sub.email, EMAILS["day_7"]["subject"], html)
            if ok:
                sub.nurture_day_7_sent = now
                sub.save(update_fields=["nurture_day_7_sent"])
                sent_count["day_7"] += 1
                self.stdout.write(self.style.SUCCESS(f"Day 7 sent to {sub.email}"))
            else:
                fail_count["day_7"] += 1
                self.stdout.write(self.style.ERROR(f"Day 7 FAILED to {sub.email}: {err}"))

        # --- Day 14: ~14d after signup, Day 7 must be sent ---
        day14_window_start = now - timedelta(days=16)
        day14_window_end = now - timedelta(days=13)
        day14_candidates = NewsletterSubscriber.objects.filter(
            is_active=True,
            nurture_unsubscribed=False,
            nurture_day_7_sent__isnull=False,
            nurture_day_14_sent__isnull=True,
            subscribed_at__gte=day14_window_start,
            subscribed_at__lte=day14_window_end,
        )
        for sub in day14_candidates:
            name = sub.first_name or "there"
            html = EMAILS["day_14"]["html"].format(name=name)
            ok, err = send_email(sub.email, EMAILS["day_14"]["subject"], html)
            if ok:
                sub.nurture_day_14_sent = now
                sub.save(update_fields=["nurture_day_14_sent"])
                sent_count["day_14"] += 1
                self.stdout.write(self.style.SUCCESS(f"Day 14 sent to {sub.email}"))
            else:
                fail_count["day_14"] += 1
                self.stdout.write(self.style.ERROR(f"Day 14 FAILED to {sub.email}: {err}"))

        self.stdout.write("\n--- SUMMARY ---")
        for day in ("day_2", "day_7", "day_14"):
            self.stdout.write(f"{day}: {sent_count[day]} sent, {fail_count[day]} failed")

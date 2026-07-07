from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import markdown
import json
import os

# ── Email sender ─────────────────────────────────────────────────────────────
from .email_sender import send_email


# ── Page views ─────────────────────────────────────────────────────────────

def home(request):
    return render(request, 'book/home.html')

def book_detail(request):
    return render(request, 'book/book_detail.html')

from django.utils.translation import gettext as _

def readiness_scorecard(request):
    questions = [
        {"id": 1, "text": _("How would you rate your current understanding of AI capabilities?"), "options": [_("No idea"), _("Basic awareness"), _("Can use ChatGPT"), _("Build with AI APIs"), _("Expert-level")]},
        {"id": 2, "text": _("Does your organization have an AI strategy?"), "options": [_("No"), _("Informal discussions"), _("Draft strategy"), _("Approved strategy"), _("Executing strategy")]},
        {"id": 3, "text": _("How many AI tools does your team use weekly?"), "options": [_("None"), _("1-2"), _("3-5"), _("5-10"), _("10+")]},
        {"id": 4, "text": _("Have you identified which tasks AI could augment in your role?"), "options": [_("No idea"), _("Vague sense"), _("Some tasks mapped"), _("Detailed workflow analysis"), _("Implemented changes")]},
        {"id": 5, "text": _("How comfortable are you evaluating AI vendor claims?"), "options": [_("Very uncomfortable"), _("Slightly uncomfortable"), _("Neutral"), _("Mostly comfortable"), _("Expert")]},
        {"id": 6, "text": _("Has your team received any AI training?"), "options": [_("None"), _("Self-directed only"), _("Some online courses"), _("Organized training"), _("Ongoing program")]},
        {"id": 7, "text": _("Do you have a budget allocated for AI tooling?"), "options": [_("No"), _("Under $1k/mo"), _("$1k-5k/mo"), _("$5k-20k/mo"), _("$20k+/mo")]},
        {"id": 8, "text": _("How do you handle AI-generated content quality?"), "options": [_("Don't use AI content"), _("Eyeball it"), _("Basic review"), _("Structured QA process"), _("Automated + human checks")]},
        {"id": 9, "text": _("Have you documented AI usage policies?"), "options": [_("No"), _("Informal guidelines"), _("Draft policy"), _("Approved policy"), _("Enforced policy")]},
        {"id": 10, "text": _("How do you stay updated on AI developments?"), "options": [_("Don't actively"), _("Social media"), _("Newsletters/blogs"), _("Industry events"), _("Academic papers")]},
        {"id": 11, "text": _("Rate your data readiness for AI integration:"), "options": [_("Chaotic"), _("Some structured"), _("Mostly organized"), _("Well-structured"), _("AI-ready pipelines")]},
        {"id": 12, "text": _("Have you measured ROI on any AI implementation?"), "options": [_("No implementations"), _("No ROI tracked"), _("Some informal tracking"), _("Basic ROI measurement"), _("Detailed ROI analysis")]},
        {"id": 13, "text": _("How does leadership view AI adoption?"), "options": [_("Skeptical/hostile"), _("Indifferent"), _("Curious"), _("Supportive"), _("Championing")]},
        {"id": 14, "text": _("Do you have an AI ethics framework?"), "options": [_("No"), _("Aware of issues"), _("Informal principles"), _("Documented framework"), _("Implemented + reviewed")]},
        {"id": 15, "text": _("How integrated is AI in your core workflows?"), "options": [_("Not at all"), _("Experimental"), _("Some processes"), _("Many processes"), _("Core to operations")]},
        {"id": 16, "text": _("Can you explain AI limitations to stakeholders?"), "options": [_("No"), _("Basic concepts"), _("Some depth"), _("Confident communicator"), _("Trusted advisor")]},
        {"id": 17, "text": _("Have you planned for AI failure modes?"), "options": [_("No"), _("Vague awareness"), _("Some contingencies"), _("Documented plans"), _("Regular drills")]},
        {"id": 18, "text": _("How do you handle AI bias and fairness?"), "options": [_("Not considered"), _("Aware of issue"), _("Basic checks"), _("Structured review"), _("Continuous monitoring")]},
        {"id": 19, "text": _("What's your AI talent situation?"), "options": [_("No expertise"), _("One interested person"), _("Small team"), _("Dedicated team"), _("Center of excellence")]},
        {"id": 20, "text": _("How future-proof do you feel your skills are?"), "options": [_("Very vulnerable"), _("Somewhat at risk"), _("Neutral"), _("Mostly secure"), _("Actively future-proofing")]}
    ]
    return render(request, 'book/scorecard.html', {"questions": questions})

def resource_calculator(request):
    context = {
        "role_options": [
            ("solo", _("Solo entrepreneur / Freelancer")),
            ("small", _("Small business owner (1-10 team)")),
            ("medium", _("Mid-size company (11-50 team)")),
            ("enterprise", _("Enterprise (50+ team)")),
        ],
        "capability_options": [
            ("llm", _("Text generation (ChatGPT, Claude)")),
            ("image", _("Image generation (Midjourney, DALL-E)")),
            ("code", _("Code assistance (GitHub Copilot)")),
            ("data", _("Data analysis (Tableau AI, Excel)")),
            ("voice", _("Voice / speech (ElevenLabs, Whisper)")),
            ("automation", _("Workflow automation (Zapier, Make)")),
        ],
        "budget_options": [
            ("low", _("Under $100/month")),
            ("mid", _("$100-500/month")),
            ("high", _("$500-2,000/month")),
            ("enterprise", _("$2,000+/month")),
        ],
        "output_options": [
            ("10", _("10-25% faster")),
            ("25", _("25-50% faster")),
            ("50", _("50-100% faster")),
            ("100", _("2x+ improvement")),
        ],
        "base_costs": {
            "llm": {"solo": 20, "small": 60, "medium": 200, "enterprise": 800},
            "image": {"solo": 30, "small": 80, "medium": 250, "enterprise": 1000},
            "code": {"solo": 10, "small": 40, "medium": 150, "enterprise": 600},
            "data": {"solo": 50, "small": 150, "medium": 500, "enterprise": 2000},
            "voice": {"solo": 20, "small": 60, "medium": 200, "enterprise": 800},
            "automation": {"solo": 20, "small": 80, "medium": 300, "enterprise": 1200}
        },
        "stack_names": {
            "llm": "ChatGPT Team / Claude Pro",
            "image": "Midjourney / DALL-E",
            "code": "GitHub Copilot",
            "data": "Tableau AI / Power BI",
            "voice": "ElevenLabs / Whisper API",
            "automation": "Zapier / Make"
        },
        "budget_multipliers": {"low": 0.7, "mid": 1.0, "high": 1.3, "enterprise": 1.8},
        "output_multipliers": {"10": 0.8, "25": 1.0, "50": 1.3, "100": 1.8},
        "hours_saved": {"10": 4, "25": 10, "50": 20, "100": 40}
    }
    return render(request, 'book/calculator.html', context)

def prompt_library(request):
    return render(request, 'book/prompt_library.html')

def community(request):
    return render(request, 'book/community.html')

def about(request):
    return render(request, 'book/about.html')

def contact(request):
    return render(request, 'book/contact.html')

def preview_index(request):
    return render(request, 'book/preview_index.html')

def chapter_preview(request, chapter_num):
    if chapter_num not in [1, 2, 3]:
        return render(request, 'book/preview_index.html')
    
    chapter_titles = {
        1: "What AI Actually Is (And What It Isn't)",
        2: "A Short History of Artificial Intelligence",
        3: "The Transformer Revolution"
    }
    
    md_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', f'ch{chapter_num}_raw.md')
    with open(md_path, 'r') as f:
        md_content = f.read()
    
    md = markdown.Markdown(extensions=['extra', 'nl2br'])
    html_content = md.convert(md_content)
    
    context = {
        'chapter_number': chapter_num,
        'chapter_title': chapter_titles[chapter_num],
        'chapter_html': html_content,
        'prev_chapter': chapter_num - 1 if chapter_num > 1 else None,
        'next_chapter': chapter_num + 1 if chapter_num < 3 else None,
    }
    return render(request, 'book/chapter_preview.html', context)


# ── API endpoints ──────────────────────────────────────────────────────────

@csrf_exempt
def api_subscribe(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        data = json.loads(request.body)
        email = data.get('email', '').strip().lower()
        first_name = data.get('first_name', '').strip()
        source = data.get('source', 'website')
        
        if not email:
            return JsonResponse({'error': 'Email required'}, status=400)
        validate_email(email)
        
        from .models import NewsletterSubscriber
        subscriber, created = NewsletterSubscriber.objects.get_or_create(
            email=email,
            defaults={'first_name': first_name, 'source': source}
        )
        
        if not created:
            subscriber.is_active = True
            if source not in (subscriber.source or ''):
                subscriber.source = f"{subscriber.source or ''},{source}"
            subscriber.save()
        
        # Send welcome email (fire-and-forget, don't fail the API call)
        if created:
            display_name = first_name if first_name else "there"
            welcome_html = f"""<!DOCTYPE html>
<html><body style="font-family:Inter,sans-serif;color:#1A1A2E;background:#FAFAF8;padding:40px 20px;">
<div style="max-width:560px;margin:0 auto;background:#fff;border-radius:12px;padding:40px;box-shadow:0 4px 20px rgba(26,35,78,0.08);">
  <h2 style="color:#1A234E;font-family:'Playfair Display',serif;margin-top:0;">Welcome to The Waiting Room</h2>
  <p>Hi {display_name},</p>
  <p>You just joined <strong>The Waiting Room</strong> — the weekly briefing that cuts through AI hype and tells you what actually matters.</p>
  <p>Here's what to expect:</p>
  <ul>
    <li><strong>Tuesday mornings:</strong> One headline decoded, one tool tested, one myth busted.</li>
    <li><strong>No fluff.</strong> If it's not actionable, it doesn't make the cut.</li>
    <li><strong>Skeptical by default.</strong> I don't get excited about press releases.</li>
  </ul>
  <p>In the meantime, here are three things worth your time:</p>
  <ol>
    <li><a href="https://morethanparrots.com/preview/1/" style="color:#B87A4A;">Read Chapter 1 free</a> — What AI Actually Is (And What It Isn't)</li>
    <li><a href="https://morethanparrots.com/readiness-scorecard/" style="color:#B87A4A;">Take the AI Readiness Scorecard</a> — 5 minutes, brutally honest</li>
    <li><a href="https://morethanparrots.com/prompt-library/" style="color:#B87A4A;">Browse the Prompt Library</a> — 200+ tested prompts for business owners</li>
  </ol>
  <p style="margin-top:30px;">The book drops soon. You'll hear about it first.</p>
  <p style="color:#6B7280;font-size:14px;margin-top:30px;">— Glen Ansell<br>Author, <em>More Than Parrots, Less Than Gods</em></p>
  <hr style="border:none;border-top:1px solid #e5e7eb;margin:30px 0;">
  <p style="font-size:12px;color:#9CA3AF;">You're receiving this because you subscribed at morethanparrots.com. <a href="https://morethanparrots.com/" style="color:#9CA3AF;">Unsubscribe</a> any time.</p>
</div>
</body></html>"""
            try:
                ok, err = send_email(email, "Welcome to The Waiting Room — your AI skeptic's briefing", welcome_html)
                if not ok:
                    print(f"[EMAIL] Welcome email failed for {email}: {err}")
            except Exception as e:
                print(f"[EMAIL] Welcome email exception for {email}: {e}")
        
        return JsonResponse({
            'success': True,
            'message': 'Subscribed!' if created else 'Already subscribed, welcome back!',
            'is_new': created
        })
    except (json.JSONDecodeError, ValidationError) as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def api_contact(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        topic = data.get('topic', 'General inquiry')
        message = data.get('message', '').strip()
        
        if not all([name, email, message]):
            return JsonResponse({'error': 'Name, email, and message required'}, status=400)
        validate_email(email)
        
        from .models import ContactMessage
        ContactMessage.objects.create(name=name, email=email, topic=topic, message=message)
        return JsonResponse({'success': True, 'message': 'Message sent!'})
    except (json.JSONDecodeError, ValidationError) as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def api_scorecard(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        data = json.loads(request.body)
        score = data.get('score', 0)
        persona = data.get('persona', 'Explorer')
        answers = data.get('answers', {})
        email = data.get('email', '').strip().lower()
        
        from .models import ScorecardResult
        submission = ScorecardResult.objects.create(
            email=email if email else None,
            score=score,
            persona=persona,
            answers=answers
        )
        
        # Send personalized scorecard email if email provided
        if email:
            display_name = data.get('first_name', '').strip() or "there"
            
            recommendations = {
                "The Explorer": {
                    "chapters": "Chapters 1–5",
                    "focus": "Build foundational understanding before making any AI investments.",
                    "action": "Start with Chapter 1 (free preview) and the AI Strategy Playbook."
                },
                "The Curious": {
                    "chapters": "Chapters 6–9, 13",
                    "focus": "You need structure and a clear implementation framework.",
                    "action": "Read the Partnership Framework and the Implementation Playbook chapters."
                },
                "The Practitioner": {
                    "chapters": "Chapters 14–17",
                    "focus": "Scaling requires governance, team building, and avoiding common traps.",
                    "action": "Deep-dive into governance frameworks and the Team Builder's Guide."
                },
                "The Architect": {
                    "chapters": "Chapters 10–12, 18–19",
                    "focus": "Even experts fall for hype. The skeptical frameworks will save you from expensive mistakes.",
                    "action": "Read the Industry Disruption chapters and the Future-Proofing sections."
                }
            }
            rec = recommendations.get(persona, recommendations["The Explorer"])
            
            score_html = f"""<!DOCTYPE html>
<html><body style="font-family:Inter,sans-serif;color:#1A1A2E;background:#FAFAF8;padding:40px 20px;">
<div style="max-width:560px;margin:0 auto;background:#fff;border-radius:12px;padding:40px;box-shadow:0 4px 20px rgba(26,35,78,0.08);">
  <h2 style="color:#1A234E;font-family:'Playfair Display',serif;margin-top:0;">Your AI Readiness Scorecard Results</h2>
  <p>Hi {display_name},</p>
  <div style="text-align:center;padding:24px;background:linear-gradient(135deg,#1A234E 0%,#0F1635 100%);border-radius:12px;color:#fff;margin:20px 0;">
    <div style="font-size:48px;font-weight:bold;color:#B87A4A;">{score}%</div>
    <div style="font-size:20px;font-weight:600;margin-top:8px;">{persona}</div>
  </div>
  <p><strong>What this means:</strong></p>
  <p>{rec['focus']}</p>
  <p><strong>Recommended reading:</strong> {rec['chapters']}</p>
  <p><strong>Next action:</strong> {rec['action']}</p>
  <div style="text-align:center;margin:30px 0;">
    <a href="https://morethanparrots.com/book/" style="display:inline-block;background:#B87A4A;color:#fff;text-decoration:none;padding:14px 32px;border-radius:8px;font-weight:500;">Pre-Order the Book</a>
  </div>
  <p style="color:#6B7280;font-size:14px;margin-top:30px;">— Glen Ansell<br>Author, <em>More Than Parrots, Less Than Gods</em></p>
  <hr style="border:none;border-top:1px solid #e5e7eb;margin:30px 0;">
  <p style="font-size:12px;color:#9CA3AF;">You completed this scorecard at morethanparrots.com.</p>
</div>
</body></html>"""
            try:
                ok, err = send_email(email, f"Your AI Readiness Result: {persona} ({score}%)", score_html)
                if not ok:
                    print(f"[EMAIL] Scorecard email failed for {email}: {err}")
            except Exception as e:
                print(f"[EMAIL] Scorecard email exception for {email}: {e}")
        
        return JsonResponse({
            'success': True,
            'id': submission.id,
            'redirect': '/book/' if score < 30 else '/prompt-library/'
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def api_calculator(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        data = json.loads(request.body)
        role = data.get('role', '')
        capabilities = data.get('capabilities', [])
        team_size = data.get('team_size', 1)
        budget_range = data.get('budget_range', '')
        output_volume = data.get('output_volume', '')
        email = data.get('email', '').strip().lower()
        
        from .models import CalculatorResult
        CalculatorResult.objects.create(
            email=email if email else None,
            role=role,
            team_size=team_size,
            budget_range=budget_range,
            output_volume=output_volume,
            capabilities=capabilities
        )
        
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def api_prompt_download(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        data = json.loads(request.body)
        prompt_name = data.get('prompt_name', '')
        email = data.get('email', '').strip().lower()
        
        from .models import PromptDownload
        PromptDownload.objects.create(
            email=email if email else None,
            prompt_name=prompt_name
        )
        
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

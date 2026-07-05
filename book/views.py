from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import markdown
import json
import os

def home(request):
    return render(request, 'book/home.html')

def book_detail(request):
    return render(request, 'book/book_detail.html')

def readiness_scorecard(request):
    return render(request, 'book/scorecard.html')

def resource_calculator(request):
    return render(request, 'book/calculator.html')

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
        
        from .models import ScorecardSubmission
        submission = ScorecardSubmission.objects.create(
            email=email if email else None,
            score=score,
            persona=persona,
            answers=answers
        )
        
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
        
        from .models import CalculatorSubmission
        submission = CalculatorSubmission.objects.create(
            email=email if email else None,
            role=role,
            team_size=team_size,
            budget_range=budget_range,
            output_volume=output_volume,
            capabilities=capabilities
        )
        
        return JsonResponse({
            'success': True,
            'id': submission.id,
        })
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

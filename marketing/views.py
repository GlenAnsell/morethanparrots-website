from django.shortcuts import render

def newsletter_signup(request):
    return render(request, 'marketing/newsletter.html')

def lead_magnet(request):
    return render(request, 'marketing/lead_magnet.html')

from django.db import models
import json

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=50, default='website', 
                              help_text='Where they signed up (e.g., homepage, scorecard, calculator)')
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    tags = models.CharField(max_length=200, blank=True, 
                            help_text='Comma-separated tags (e.g., scorecard-completed, buyer-intent)')
    
    # Nurture sequence tracking
    nurture_day_2_sent = models.DateTimeField(blank=True, null=True)
    nurture_day_7_sent = models.DateTimeField(blank=True, null=True)
    nurture_day_14_sent = models.DateTimeField(blank=True, null=True)
    nurture_unsubscribed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-subscribed_at']
    
    def __str__(self):
        return self.email

class ScorecardResult(models.Model):
    session_id = models.CharField(max_length=64, db_index=True)
    answers = models.JSONField(default=dict)
    score = models.IntegerField()
    persona = models.CharField(max_length=50)
    persona_description = models.TextField(blank=True)
    recommended_chapters = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.persona} ({self.score})"

class CalculatorResult(models.Model):
    session_id = models.CharField(max_length=64, db_index=True)
    role = models.CharField(max_length=50)
    capabilities = models.JSONField(default=list)
    budget_tier = models.CharField(max_length=50)
    output_increase = models.CharField(max_length=50)
    recommended_monthly_budget = models.IntegerField()
    suggested_stack = models.JSONField(default=list)
    break_even_months = models.IntegerField()
    annual_hours_saved = models.IntegerField()
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    topic = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} — {self.topic}"

class PromptDownload(models.Model):
    email = models.EmailField()
    downloaded_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=50, default='prompt_library')
    
    class Meta:
        ordering = ['-downloaded_at']

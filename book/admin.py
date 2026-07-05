from django.contrib import admin
from .models import NewsletterSubscriber, ScorecardResult, CalculatorResult, ContactMessage, PromptDownload

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'source', 'subscribed_at', 'is_active']
    list_filter = ['source', 'is_active', 'subscribed_at']
    search_fields = ['email', 'first_name']
    date_hierarchy = 'subscribed_at'

@admin.register(ScorecardResult)
class ScorecardResultAdmin(admin.ModelAdmin):
    list_display = ['persona', 'score', 'email', 'created_at']
    list_filter = ['persona', 'created_at']
    search_fields = ['email', 'session_id']

@admin.register(CalculatorResult)
class CalculatorResultAdmin(admin.ModelAdmin):
    list_display = ['role', 'recommended_monthly_budget', 'email', 'created_at']
    list_filter = ['role', 'budget_tier', 'created_at']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'topic', 'created_at', 'is_read']
    list_filter = ['topic', 'is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']

@admin.register(PromptDownload)
class PromptDownloadAdmin(admin.ModelAdmin):
    list_display = ['email', 'source', 'downloaded_at']
    list_filter = ['source', 'downloaded_at']

from django.urls import path
from . import views

app_name = 'marketing'

urlpatterns = [
    path('newsletter/', views.newsletter_signup, name='newsletter'),
    path('lead-magnet/', views.lead_magnet, name='lead_magnet'),
]

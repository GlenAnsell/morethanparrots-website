from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_detail, name='book_detail'),
    path('readiness-scorecard/', views.readiness_scorecard, name='scorecard'),
    path('resource-calculator/', views.resource_calculator, name='calculator'),
    path('prompt-library/', views.prompt_library, name='prompt_library'),
    path('community/', views.community, name='community'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('preview/', views.preview_index, name='preview_index'),
    path('preview/<int:chapter_num>/', views.chapter_preview, name='chapter_preview'),
    path('api/subscribe/', views.api_subscribe, name='api_subscribe'),
    path('api/contact/', views.api_contact, name='api_contact'),
    path('api/scorecard/', views.api_scorecard, name='api_scorecard'),
    path('api/calculator/', views.api_calculator, name='api_calculator'),
    path('api/prompt-download/', views.api_prompt_download, name='api_prompt_download'),
]

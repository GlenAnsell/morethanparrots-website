# Generated manually 2026-07-05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('excerpt', models.TextField(blank=True, help_text='Shown in listings and meta description. Max 300 chars.')),
                ('body', models.TextField(help_text='Markdown supported. HTML will be sanitized on save.')),
                ('body_html', models.TextField(blank=True, editable=False)),
                ('category', models.CharField(choices=[('ai-explained', 'AI Explained'), ('business-strategy', 'Business Strategy'), ('hype-vs-reality', 'Hype vs Reality'), ('tools-tutorials', 'Tools & Tutorials'), ('for-parents', 'For Parents'), ('future-of-work', 'Future of Work')], default='ai-explained', max_length=30)),
                ('featured_image', models.ImageField(blank=True, upload_to='blog/')),
                ('published', models.BooleanField(default=False)),
                ('published_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('meta_title', models.CharField(blank=True, help_text='Override <title> tag. Max 70 chars.', max_length=70)),
                ('meta_description', models.CharField(blank=True, help_text='SEO meta description. Max 160 chars.', max_length=160)),
                ('reading_time_minutes', models.PositiveIntegerField(default=5)),
            ],
            options={
                'ordering': ['-published_at', '-created_at'],
            },
        ),
    ]

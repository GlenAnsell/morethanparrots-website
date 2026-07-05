from django.db import models
from django.urls import reverse
import bleach


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('ai-explained', 'AI Explained'),
        ('business-strategy', 'Business Strategy'),
        ('hype-vs-reality', 'Hype vs Reality'),
        ('tools-tutorials', 'Tools & Tutorials'),
        ('for-parents', 'For Parents'),
        ('future-of-work', 'Future of Work'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    excerpt = models.TextField(help_text="Shown in listings and meta description. Max 300 chars.", blank=True)
    body = models.TextField(help_text="Markdown supported. HTML will be sanitized on save.")
    body_html = models.TextField(blank=True, editable=False)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='ai-explained')
    featured_image = models.ImageField(upload_to='blog/', blank=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_title = models.CharField(max_length=70, blank=True, help_text="Override <title> tag. Max 70 chars.")
    meta_description = models.CharField(max_length=160, blank=True, help_text="SEO meta description. Max 160 chars.")
    reading_time_minutes = models.PositiveIntegerField(default=5)

    class Meta:
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        allowed_tags = [
            'p', 'br', 'strong', 'b', 'em', 'i', 'u', 'h1', 'h2', 'h3', 'h4',
            'ul', 'ol', 'li', 'a', 'blockquote', 'code', 'pre', 'hr',
            'img', 'figure', 'figcaption', 'table', 'thead', 'tbody', 'tr', 'th', 'td'
        ]
        allowed_attrs = {
            '*': ['class'],
            'a': ['href', 'title', 'target', 'rel'],
            'img': ['src', 'alt', 'title', 'width', 'height'],
        }
        self.body_html = bleach.clean(self.body, tags=allowed_tags, attributes=allowed_attrs, strip=True)
        super().save(*args, **kwargs)

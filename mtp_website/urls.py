from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.http import HttpResponse
from blog.sitemaps import BlogSitemap

sitemaps = {
    'blog': BlogSitemap,
}


def robots_txt(request):
    lines = [
        'User-agent: *',
        'Allow: /',
        'Sitemap: https://morethanparrots.com/sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')


# Non-i18n URLs (sitemap, robots, admin, etc.)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),
]

# i18n URLs with language prefix
urlpatterns += i18n_patterns(
    path('', include('book.urls')),
    path('blog/', include('blog.urls')),
    path('', include('marketing.urls')),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

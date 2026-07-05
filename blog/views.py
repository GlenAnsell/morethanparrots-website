from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published=True).select_related()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    categories = Post.CATEGORY_CHOICES
    return render(request, 'blog/post_list.html', {
        'page_obj': page_obj,
        'categories': categories,
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    related = Post.objects.filter(
        published=True, category=post.category
    ).exclude(id=post.id)[:3]
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'related_posts': related,
    })


def category_list(request, category):
    posts = Post.objects.filter(published=True, category=category)
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    category_label = dict(Post.CATEGORY_CHOICES).get(category, category)
    return render(request, 'blog/category.html', {
        'page_obj': page_obj,
        'category': category,
        'category_label': category_label,
    })

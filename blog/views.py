from django.shortcuts import render

from .models import Category, Post

def index(request):
    posts = Post.objects.order_by('-creation_date')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404('Post does not exist!')
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)

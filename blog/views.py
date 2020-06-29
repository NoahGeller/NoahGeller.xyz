from django.shortcuts import render, get_object_or_404

from .models import Tag, Post

def index(request):
    posts = Post.objects.order_by('-pub_date')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)

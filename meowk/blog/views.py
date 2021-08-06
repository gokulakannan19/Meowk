from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)


# def blog(request):
    #     context = {}
#     return render(request, 'blog/blog.html', context)

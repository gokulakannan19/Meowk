from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {}
    return render(request, 'blog/home.html', context)


def blog(request):
    context = {}
    return render(request, 'blog/blog.html', context)


def post(request):
    context = {}
    return render(request, 'blog/post.html', context)

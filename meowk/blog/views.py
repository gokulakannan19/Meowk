from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Post, Blogger
from .forms import PostForm


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


def create_post(request):

    form = PostForm()
    if request. method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'blog/create-post.html', context)


def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'blog/update-post.html', context)


def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'blog/delete-post.html')
# def blogger(request, pk):
#     blogger = Blogger.objects.get(id=pk)
#     context = {
#         'blogger': blogger
#     }
#     return render(request, 'blog/blog.html', context)

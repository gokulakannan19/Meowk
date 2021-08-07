from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Post, Blogger
from .forms import PostForm, CreateUserForm


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('usernmae')
                messages.success(request, "Account was successfully created")
                return redirect('login-user')

        context = {
            'form': form
        }
        return render(request, 'blog/register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or password is incorrect")

        context = {}
        return render(request, 'blog/login.html', context)


@login_required(login_url='login-user')
def logout_user(request):
    logout(request)
    return redirect('login-user')


def home(request):
    posts = Post.objects.all().order_by('date_created',)[::-1]
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

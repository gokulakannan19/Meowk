from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("home")


def blog(request):
    return HttpResponse("Blog")


def post(request):
    return HttpResponse("Post")

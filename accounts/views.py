from django.shortcuts import render, render, redirect, HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    template_name = "accounts/index.html"
    args = {}
    return render(request,template_name,args)

def signup(request):
    template_name = "accounts/signup.html"
    args = {}
    return render(request,template_name,args)

def login(request):
    template_name = "accounts/login.html"
    args = {}
    return render(request,template_name,args)

def questions(request):
    template_name = "accounts/question.html"
    args = {}
    return render(request,template_name,args)
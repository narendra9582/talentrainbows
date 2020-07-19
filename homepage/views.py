from django.shortcuts import render,redirect
from django.contrib import messages
from users import views

def index(request):
    return render(request,'users/signup.html')

def homepage(request):
    return render(request,'homepage/homepage.html')
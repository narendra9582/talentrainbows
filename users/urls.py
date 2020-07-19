from django.contrib import admin
from django.urls import path, include
import users.views

urlpatterns = [
    path('login',users.views.loginUser,name = "login"),
    path('signup',users.views.signupUser,name = "signup"),
    path('logout',users.views.logoutUser,name = "logout"),
]
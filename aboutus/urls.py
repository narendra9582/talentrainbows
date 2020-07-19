from django.contrib import admin
from django.urls import path, include
from aboutus import views
import aboutus

urlpatterns = [
    path('aboutus',aboutus.views.aboutus,name = "aboutus"),
]
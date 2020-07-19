from django.contrib import admin
from django.urls import path, include
import services.views

urlpatterns = [
    path('services',services.views.services, name = "services"),
]
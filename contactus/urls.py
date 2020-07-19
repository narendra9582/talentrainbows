from django.contrib import admin
from django.urls import path, include
import contactus.views

urlpatterns = [
    path('contactus',contactus.views.contactus),
]
from django.contrib import admin
from django.urls import path, include
import newitems.views

urlpatterns = [
    path('newitems',newitems.views.newitems,name = "new Items"),
]
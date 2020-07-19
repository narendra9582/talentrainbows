from django.contrib import admin
from django.urls import path, include
from homepage import urls
from users import urls
from newitems import urls
from services import urls
from contactus import urls
from aboutus import urls

admin.site.site_header = "Talentrainbows Admin"
admin.site.site_title = "Talentrainbows Admin Portal"
admin.site.index_title = "Welcome to talentrainbows 'A Place to show your talent :)"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls')),
    path('',include('users.urls')),
    path('',include('newitems.urls')),
    path('',include('services.urls')),
    path('',include('aboutus.urls')),
    path('',include('contactus.urls')),
]
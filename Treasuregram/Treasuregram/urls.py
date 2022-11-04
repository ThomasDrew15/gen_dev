"""Treasuregram URL Configuration"""

from django.urls import include, re_path
from django.contrib import admin
from main_app import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    #localhost:8000 will direct here:
    re_path(r'^',
            include('main_app.urls')),
]

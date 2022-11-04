"""Treasuregram URL Configuration"""

from django.conf.urls import url
from django.contrib import admin
from main_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    url(r'^index/',
        views.index),
]

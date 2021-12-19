from django.contrib import admin
from django.urls import path
from searchapp import views
from django.urls import path, include


urlpatterns = [
    path ('', views.home , name = 'home'),


]
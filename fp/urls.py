from django.contrib import admin
from django.urls import path
from fp import views

urlpatterns = [
    path('', views.home, name='home'),
]
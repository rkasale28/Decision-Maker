from django.contrib import admin
from django.urls import path
from preferences import views

urlpatterns = [
    path('fp', views.fp, name='home'),
]
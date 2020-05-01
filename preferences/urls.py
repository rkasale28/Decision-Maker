from django.contrib import admin
from django.urls import path
from preferences import views

urlpatterns = [
    path('fp', views.fp, name='fp'),
    path('sp', views.sp, name='sp'),
    path('tp', views.tp, name='tp'),
    path('fop', views.fop, name='fop'),
    path('fip', views.fip, name='fip'),
    path('sip', views.sip, name='sip'),
]
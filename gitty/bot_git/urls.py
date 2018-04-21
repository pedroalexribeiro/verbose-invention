from django.contrib import admin
from django.urls import path
from . import views

app_name = 'bot'
urlpatterns = [
    path('', views.callback, name='tryout'),
]
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'bot_gitty'
urlpatterns = [
    path('', views.callback, name='tryout'),
]
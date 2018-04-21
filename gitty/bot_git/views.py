from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def callback(request, data):
    return HttpResponse("This is what I received: %s." %data)
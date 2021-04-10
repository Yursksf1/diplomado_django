from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    print('estoy llamando al index')
    return HttpResponse('hello')
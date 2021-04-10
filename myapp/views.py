from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject

# Create your views here.


def subject(request):
    subjects = Subject.objects.all()
    response = ''
    for subject in subjects:
        print(subject.name)
        response = response + ' ' + subject.name

    print('estoy llamando al index')
    return HttpResponse(response)
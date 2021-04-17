from django.contrib import admin
from django.urls import path
from .views import list_teachers, list_students, subject, students

urlpatterns = [
    path('list_students', list_students),
    path('list_teachers', list_teachers),
    path('subject', subject),
    path('students', students),
]

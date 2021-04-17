from django.contrib import admin
from django.urls import path
from .views import index_2, index, subject, students

urlpatterns = [
    path('', index),
    path('2', index_2),
    path('subject', subject),
    path('students', students),
]

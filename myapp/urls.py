from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list_students', views.list_students),
    path('list_teachers', views.list_teachers),
    path('subject', views.subject),
    path('students', views.students),

    path('example/<person>/', views.list_person),
    path('example/<person>/<id>', views.get_person),
]

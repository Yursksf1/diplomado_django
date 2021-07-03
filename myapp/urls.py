from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list_students', views.list_students),
    path('list_teachers', views.list_teachers, name='teachers'),
    path('subject', views.subject),

    path('students', views.students, name='students'),
    path('students/<id>', views.get_student, name='get_student'),

    path('example/<person>/', views.list_person),
    path('example/<person>/<id>', views.get_person),

    path('groups', views.list_group,  name='groups'),
    path('group/new', views.new_group, name='new_group'),
    path('group/<id>', views.get_group, name='get_group'),
]

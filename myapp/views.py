from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Subject, Student

# Create your views here.


def subject(request):
    subjects = Subject.objects.all()
    response = ''
    for subject in subjects:
        print(subject.name)
        response = response + ' ' + subject.name

    print('estoy llamando al index')
    return HttpResponse(response)


def students(request):
    students = Student.objects.all()
    response = {}
    for student in students:
        print(student.first_name, student.last_name)
        response[student.id] = {
            'full name': '{} {}'.format(student.first_name, student.last_name),
        }
        enrollments = student.enrollment_set.all()
        student_enrollment = []

        for enrollment in enrollments:
            student_enrollment.append(enrollment.subject.name)

        response[student.id]['enrollments'] = student_enrollment
        # TODO: add promedio por materia y por cada estudiante


    print('response', response)

    return JsonResponse(response)
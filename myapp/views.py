from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Subject, Student, Teacher

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
    response = get_students()
    return JsonResponse(response)


def get_students():
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

            average_enrollment = 0
            notes = enrollment.note_set.all()
            if notes:
                for note in notes:
                    average_enrollment = average_enrollment + note.value

                average_enrollment = average_enrollment / len(notes)
            student_enrollment.append(
                {
                    'name': enrollment.subject.name,
                    'average': average_enrollment
                }
            )

        response[student.id]['enrollments'] = student_enrollment
    return response


def list_students(request):
    students = Student.objects.all()
    context = {
        'title': 'Estudiantes',
        'students': students
    }

    return render(request, 'list_students.html', context)


def list_teachers(request):
    teachers = Teacher.objects.all()
    context = {
        'title': 'Profesores',
        'teachers': teachers
    }

    return render(request, 'list_teachers.html', context)


def list_person(request, person):
    models = Student
    if person == 'teacher':
        models = Teacher

    persons = models.objects.all()
    context = {
        'title': person,
        'persons': persons
    }
    return render(request, 'list_person.html', context)


def get_person(request, person, id):
    models = Student
    if person == 'teacher':
        models = Teacher

    persons = models.objects
    person = persons.filter(id=id).first()
    context = {
        'title': person,
        'person': person
    }
    return render(request, 'person_detail.html', context)


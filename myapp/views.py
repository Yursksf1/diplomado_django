from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import Subject, Student, Teacher, Group
from .forms import GroupForm, StudenFrom
# Create your views here.


def home(request):
    context = {}
    print('estoy llamando al index')
    return render(request, 'new_group.html', context)

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


def list_group(request):
    groups = Group.objects.all()
    context = {
        'title': 'Groups',
        'groups': groups
    }

    return render(request, 'list_groups.html', context)


def get_group(request, id):

    group = Group.objects.filter(id=id).first()
    students = group.student_set.all()
    context = {
        'title': group.title,
        'group': group,
        'students': students
    }

    return render(request, 'detail_group.html', context)


def get_student(request, id):
    student = Student.objects.filter(id=id).first()
    groups = student.group.all()
    context = {
        'title': 'student',
        'groups': groups,
        'student': student
    }

    return render(request, 'detail_student.html', context)


def new_group(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST)

        if form.is_valid():
            description = form.cleaned_data['description']
            title = form.cleaned_data['title']

            Group(title=title, description=description).save()
            return redirect('groups')

    return render(request, 'new_group.html', {'form': form})

def new_student(request):
    form = StudenFrom()
    if request.method == 'POST':
        form = StudenFrom(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            Student(first_name=first_name, last_name=last_name).save()
            return redirect('students')

    return render(request, 'new_student.html', {'form': form})


def new_group_2(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        title = request.POST.get('title')

        Group(title=title, description=description).save()
        return redirect('groups')

    return render(request, 'new_group.html')

from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login as auth_login


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)

            return redirect('saludo')

    return render(request, 'login.html')


def saludo(request):
    return render(request, 'saludo.html')

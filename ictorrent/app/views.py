from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

def home(request):
    files = File.objects.all()
    return render(request, 'home.html', {'files':files})

@csrf_protect
def register_user(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username = username, password = password)

        if user is not None:
            print(user)
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Ocorreu algo inesperado')
            return redirect('/register')
    else:
        return redirect('/register')
from django.shortcuts import render, redirect
from .forms import *


def index(request):
    return render(request, 'account/home.html')


def login(request):
    form = LoginForm
    return render(request, 'account/login.html', {'form': form})


def register(request):
    return render(request, 'account/register.html')


def logout(request):
    form = LoginForm
    return render(request, 'account/login.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages


def index(request):
    return render(request, 'account/home.html')


def login(request):
    if 'logged_in' in request.session:
        if request.session['logged_in'] is True:
            return redirect('account:index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = User.objects.get(username=username)
            except Exception as ex:
                print(ex)
                user = None
            if user is None:
                messages.error(request, 'Username Mismatch!')
                return redirect('account:login')
            else:
                if user.password == password:
                    request.session['logged_in'] = True
                    request.session['username'] = user.username
                    request.session['id'] = user.pk
                    return redirect("account:index")
                else:
                    messages.error(request, 'Incorrect Password!')
                    return redirect('account:login')
        return render(request, 'account/login.html')


def register(request):
    return render(request, 'account/register.html')


def forgot_password(request):
    return redirect('account:index')


def logout(request):
    return redirect('account:index')

from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages


def index(request):
    if 'logged_in' in request.session:
        if request.session['logged_in'] is True:
            userdata = {
                'username': request.session['username'],
                'logged_in': request.session['logged_in'],
            }
            context = {
                'data': userdata
            }
            return render(request, 'account/home.html', context)
    return render(request, 'account/home.html')


def login(request):
    if 'logged_in' in request.session:
        if request.session['logged_in'] is True:
            return redirect('account:index')
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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_again = request.POST['password-again']
        email = request.POST['email']
        if password != password_again:
            messages.error(request, 'Password did not match. Try again.')
            return render(request, 'account/register.html')
        try:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is already taken.')
                return render(request, 'account/register.html')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email id is already taken.')
                return render(request, 'account/register.html')
            User.objects.create(username=username, password=password, email=email, role=Role.objects.get(id=2))
        except Exception as ex:
            print(ex)
            messages.error(request, 'Sorry !!! Something Went Wrong.')
            return render(request, 'account/register.html')
        return redirect('account:login')
    return render(request, 'account/register.html')


def change_email(request):
    try:
        if 'logged_in' in request.session:
            if request.session['logged_in'] is True:
                if request.method == 'POST':
                    current = request.POST['current']
                    new = request.POST['new']
                    password = request.POST['password']
                    user = User.objects.get(pk=request.session['id'])
                    if user.password == password:
                        if current == user.email:
                            user.email = new
                            user.save()
                            messages.success(request, 'Email Updated Successfully')
                            return redirect('account:index')
                        else:
                            messages.error(request, 'Email Mismatched')
                            return redirect('account:change_email')
                    else:
                        messages.error(request, 'Wrong Password')
                        return redirect('account:change_email')
                return render(request, 'account/change_email.html')
        else:
            return redirect('account:login')
    except Exception as ex:
        messages.error(request, str(ex))
        return redirect('account:login')


def change_password(request):
    try:
        if 'logged_in' in request.session:
            if request.session['logged_in'] is True:
                if request.method == 'POST':
                    current = request.POST['current']
                    new = request.POST['new']
                    confirm = request.POST['confirm']
                    user = User.objects.get(pk=request.session['id'])
                    if user.password == current:
                        if new == confirm:
                            user.password = new
                            user.save()
                            messages.success(request, 'Password Updated Successfully')
                            return redirect('account:index')
                        else:
                            messages.error(request, 'Password Mismatched')
                            return redirect('account:change_password')
                    else:
                        messages.error(request, 'Wrong Password')
                        return redirect('account:change_password')
                return render(request, 'account/change_password.html')
        else:
            return redirect('account:login')
    except Exception as ex:
        messages.error(request, str(ex))
        return redirect('account:login')


def forgot_password(request):
    return redirect('account:index')


def logout(request):
    request.session['logged_in'] = False
    return redirect('account:index')

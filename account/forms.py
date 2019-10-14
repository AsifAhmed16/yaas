from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length='30', label='User ID')
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'type': 'password'}))


class RegisterForm(forms.Form):
    username = forms.CharField(max_length='30', label='User ID')
    email = forms.CharField(label='E-Mail', widget=forms.TextInput(attrs={'type': 'email'}))
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'type': 'password'}))

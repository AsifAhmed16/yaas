from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length='30', label='User ID')
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'type': 'password'}))

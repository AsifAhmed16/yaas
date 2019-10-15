from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('signup/', login, name='login'),
    path('register/', register, name='register'),
    path('change_email/', change_email, name='change_email'),
    path('change_password/', change_password, name='change_password'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('logout/', logout, name='logout'),
]

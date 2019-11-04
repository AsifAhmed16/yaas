from django.urls import path
from .views import *

urlpatterns = [
    path('language_test/', store_language_list, name='list'),
    path('create/', auction_add, name='auction_add'),
]

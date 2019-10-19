from django.urls import path
from .views import *

app_name = 'auction'

urlpatterns = [
    path('auction/create/', auction_add, name='auction_add'),
    path('auction/create/<int:id>/', auction_confirm, name='auction_confirm'),
]

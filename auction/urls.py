from django.urls import path
from .views import *

app_name = 'auction'

urlpatterns = [
    path('create/', auction_add, name='auction_add'),
    path('create/<int:id>/', auction_confirm, name='auction_confirm'),
    path('browse/', auction_browse, name='auction_browse'),
    path('list/', auction_list, name='auction_list'),
    path('banned/list/', banned_auctions_list, name='banned_auctions_list'),
    path('test_data/', data_generation, name='data_generation'),
    path('generate_user/', generate_user, name='generate_user'),
    path('generate_auction/', generate_auction, name='generate_auction'),
    path('generate_bid/', generate_bid, name='generate_bid'),
    path('edit/<int:id>/', auction_edit, name='auction_edit'),
    path('bid/<int:id>/', auction_bid, name='auction_bid'),
    path('ban/<int:id>/', auction_ban, name='auction_ban'),
    path('search_auction/<search>/', search_auction, name='search_auction'),
    path('convert/<bid_amount>/<currency>/', auction_convert, name='auction_convert'),
]

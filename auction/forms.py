from django import forms
from .models import *


# class AuctionForm(forms.ModelForm):
#     class Meta:
#         model = Auction
#         fields = '__all__'
#         exclude = ('seller', 'status', 'deadline', 'created_date')
#         widgets = {
#             "title": forms.TextInput(attrs={'class': 'form-control'}),
#             "description": forms.Textarea(attrs={'class': 'form-control'}),
#             "min_price": forms.NumberInput(attrs={'class': 'form-control'}),
#             # "deadline": forms.DateTimeInput(attrs={'placeholder': 'dd.mm.YY HH:MM:SS', 'required': 'required'}),
#         }


class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = '__all__'
        exclude = ('title', 'min_price', 'seller', 'status', 'deadline', 'created_date')
        widgets = {
            "description": forms.Textarea(attrs={'class': 'form-control'}),
        }


class AuctionTempForm(forms.ModelForm):
    class Meta:
        model = Auction_Temp
        fields = '__all__'
        exclude = ('seller', )
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            "min_price": forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = '__all__'
        exclude = ('auction', 'bidder', 'created_date')
        widgets = {
            "bid_price": forms.NumberInput(attrs={'class': 'form-control'}),
        }

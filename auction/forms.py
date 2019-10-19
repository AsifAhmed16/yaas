from django import forms
from .models import *


class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = '__all__'
        exclude = ('seller', 'status', 'deadline', 'created_date')
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            "min_price": forms.NumberInput(attrs={'class': 'form-control'}),
            # "deadline": forms.DateTimeInput(attrs={'placeholder': 'dd.mm.YY HH:MM:SS', 'required': 'required'}),
        }


class AuctionTempForm(forms.ModelForm):
    class Meta:
        model = Auction_Temp
        fields = '__all__'
        exclude = ('seller', )
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            "min_price": forms.NumberInput(attrs={'class': 'form-control'}),
        }

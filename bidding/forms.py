from django.forms import ModelForm
from django import forms
from .models import Bid, Item

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['price']

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'min_price']

class BidCompareForm(forms.Form):
    bid_price = forms.IntegerField()

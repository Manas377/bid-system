from django.forms import forms, ModelForm
from .models import Bid, Item

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['price']

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price']

class BidCompareForm(forms.Form):
    bid_price = forms.IntegerField()

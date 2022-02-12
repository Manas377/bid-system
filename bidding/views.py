from pyexpat import model
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Item, Bid

# Create your views here.

# def home(request):
#     return render(request, 'bidding/home.html', )

class ItemListView(ListView):
    model = Item

class ItemDetailView(DetailView):
    model = Item

class BidListView(ListView):
    model = Bid

class BidDetailView(DetailView):
    model = Bid

def bid_compare(request):
    if request.method == 'GET':
        bid_price = request.GET.get('bid_price')
        if bid_price:
            pass

        labels = []
        data = []
        Pallete = []

        queryset = Bid.objects.order_by('-price')[:10] # List top 10 bids
        for bid in queryset:
            labels.append(bid.price)
            data.append(Bid.objects.filter(price=bid.price).count())
        

        context = {
            'labels': labels,
            'data': data,
        }

        return render(request, 'bidding/bid-compare.html', context=context)
from pyexpat import model
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import redirect, render

from bidding.forms import BidCompareForm, BidForm
from .models import Item, Bid

# Create your views here.

# def home(request):
#     return render(request, 'bidding/home.html', )

class ItemListView(ListView):
    model = Item

class ItemDetailView(DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = BidForm()

        context['prev_bids'] = Bid.objects.filter(item=context['object'], buyer=self.request.user)

        return context

    def post(self, request, *args, **kwargs):
        form = BidForm(request.POST)
        if form.is_valid():
            ins = form.save(commit=False)
            ins.buyer = request.user
            ins.item_id = kwargs['pk']
            
            if ins.item.min_price > ins.price:

                messages.warning(request, "Bid price cannot be less than Minium asking price")
                return redirect(self.request.path_info)
            
            ins.save()
  
        else:
            print(form.errors)
        
        return redirect(self.request.path_info)

class BidListView(ListView):
    model = Bid

class BidDetailView(DetailView):
    model = Bid

class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'min_price']


def bid_compare(request):
    if request.method == 'GET':
        bid_price = request.GET.get('bid_price')
        form = BidCompareForm()
        if bid_price:
            print(bid_price)

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
            'form': form,
        }

        return render(request, 'bidding/bid-compare.html', context=context)
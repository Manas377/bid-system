from django.urls import path
from . import views

app_name = 'bidding'

urlpatterns = [
    path('item-list/', views.ItemListView.as_view(), name='item-list'),
    path('bid-list/', views.BidListView.as_view(), name='bid-list'),
    path('item-detail/', views.ItemDetailView.as_view(), name='item-detail'),
    path('bid-detail/', views.BidDetailView.as_view(), name='bid-detail'),
    path('bid-compare/', views.bid_compare, name='bid-compare')
]


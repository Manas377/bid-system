from django.urls import path
from . import views

app_name = 'bidding'

urlpatterns = [
    path('item-list/', views.ItemListView.as_view(), name='item-list'),
    path('bid-list/', views.BidListView.as_view(), name='bid-list'),
    path('item-detail/<int:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('bid-detail/<int:pk>/', views.BidDetailView.as_view(), name='bid-detail'),
    path('bid-compare/', views.bid_compare, name='bid-compare')
]


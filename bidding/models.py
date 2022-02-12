from django.db import models
from django.contrib.auth.models import User

from django.db.models import Max, Min

# Create your models here.


class Item(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    min_price = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

class Bid(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()

    @staticmethod
    def get_min_bid():
        bid = Bid.objects.all().aggregate(bid_min = Min('price'))
        return bid['bid_min']

    @staticmethod
    def get_max_bid():
        bid = Bid.objects.all().aggregate(bid_max = Max('price'))
        return bid['bid_max']

    def __str__(self):
        return f'{self.item.name} || Min-Bid: {self.get_min_bid()} | Max-Bid: {self.get_max_bid()} | {self.price}'
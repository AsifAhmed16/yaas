from django.db import models
from account.models import User
from auction.models import Auction


class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_price = models.DecimalField(max_digits=11, decimal_places=2)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.bid_price

    class Meta:
        db_table = 'Bid'

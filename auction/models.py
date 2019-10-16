from django.db import models
from account.models import User


class Auction_Status(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'Auction_Status'


class Auction(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=3000)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    min_price = models.DecimalField(max_digits=11, decimal_places=2)
    status = models.ForeignKey(Auction_Status, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    created_date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Auction'
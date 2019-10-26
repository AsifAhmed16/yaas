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
    version = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def as_json(self):
        return dict(
            id=str(self.id),
            title=str(self.title),
            description=str(self.description),
            min_price=str(self.min_price),
            deadline=str(self.deadline),
        )

    class Meta:
        db_table = 'Auction'


class Auction_Temp(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=3000)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    min_price = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Auction_Temp'


class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_price = models.DecimalField(max_digits=11, decimal_places=2)
    created_date = models.DateTimeField()
    version = models.IntegerField(default=0)

    def __int__(self):
        return self.auction_id

    class Meta:
        db_table = 'Bid'

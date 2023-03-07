# from djongo.models.indexes import TextIndex
from djongo import models
from datetime import datetime

from django.utils.timezone import make_aware


class Sale(models.Model):
    _id = models.ObjectIdField()
    address_city = models.CharField(max_length=150)
    address_street = models.CharField(max_length=255)
    date_sold = models.DateTimeField()
    address_state = models.CharField(max_length=3)
    address_zipcode = models.CharField(max_length=5)
    area = models.IntegerField()
    baths = models.IntegerField()
    beds = models.IntegerField()
    home_type = models.CharField(max_length=5)
    lot_area = models.IntegerField()
    sold_price = models.IntegerField()
    creation_date = models.DateTimeField()

    def __str__(self):
        return self.address_street

    class Meta:
        db_table = 'houses_coll'
        indexes = [
            # TextIndex(fields=['name'])
        ]

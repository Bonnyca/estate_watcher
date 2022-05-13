# from djongo.models.indexes import TextIndex
from djongo import models


class Sale(models.Model):
    address_city = models.CharField(max_length=150)
    address_street = models.CharField(max_length=250)
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

    class Meta:
        db_table = 'houses_coll_test'
        indexes = [
            # TextIndex(fields=['name'])
        ]

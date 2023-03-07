import django_filters
from django_filters import rest_framework as filters
from models import Sale


class MedianFilter(django_filters.FilterSet):
    date = filters.RangeFilter()

    class Meta:
        model = Sale
        # fields = ['date_sold', 'home_type', 'address_zipcode']
        exclude = ('_id', 'creation_date')
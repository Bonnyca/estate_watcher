from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework import viewsets
from .models import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
        # exclude = ['creation_date', 'date_sold']



class SalesViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()

    def get_queryset(self):
        res = Sale.objects.filter(address_street='221 Ruby Ave')
        print(res)
        return res


# def index(request):
#     print(request)
#
#
#
#     return HttpResponse(Sale.objects.all())
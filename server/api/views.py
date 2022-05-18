from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework import viewsets
from .models import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('address_city', 'address_street')



class SalesViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()



# def index(request):
#     print(request)
#
#
#
#     return HttpResponse(Sale.objects.all())
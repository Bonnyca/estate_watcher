from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
import datetime
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.utils import timezone
from .models import Sale
from .serializers import SaleSerializer



class SalesViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()

    def get_queryset(self):
        queryset = Sale.objects.all()
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        current_tz = timezone.get_current_timezone()

        try:
            date_from = datetime.datetime.strptime(date_from, '%Y-%m-%d')
        except ValueError:
            raise ValidationError(detail='Invalid date_from', code=status.HTTP_400_BAD_REQUEST)

        try:
            date_to = datetime.datetime.strptime(date_to, '%Y-%m-%d')
        except ValueError:
            raise ValidationError(detail='Invalid date_to', code=status.HTTP_400_BAD_REQUEST)

        date_from = date_from.replace(tzinfo=current_tz)
        date_to = date_to.replace(tzinfo=current_tz)

        queryset = queryset.filter(date_sold__gte=date_from).filter(date_sold__lte=date_to)
        print(len(list(queryset)))

        return queryset


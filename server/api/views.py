from django.shortcuts import render
from django.http import HttpResponse
from .models import Sale

# Create your views here.

def index(request):
    print(request)



    return HttpResponse(Sale.objects.all())
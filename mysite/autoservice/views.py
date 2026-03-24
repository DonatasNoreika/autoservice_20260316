from django.shortcuts import render
from .models import Service, Car, Order

def index(request):
    context = {
        'services': Service.objects.count(),
        'cars': Car.objects.count(),
        'orders_done': Order.objects.filter(status='c').count(),
    }
    return render(request, template_name="index.html", context=context)

def cars(request):
    context = {
        'cars': Car.objects.all(),
    }
    return render(request, template_name="cars.html", context=context)
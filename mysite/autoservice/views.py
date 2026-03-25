from django.shortcuts import render
from .models import Service, Car, Order
from django.views import generic

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


def car(request, car_pk):
    context = {
        'car': Car.objects.get(pk=car_pk)
    }
    return render(request, template_name="car.html", context=context)


class OrderListView(generic.ListView):
    model = Order
    template_name = "orders.html"
    context_object_name = "orders"
    paginate_by = 2


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'

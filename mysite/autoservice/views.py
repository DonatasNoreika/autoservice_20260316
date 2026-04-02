from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.views.generic.edit import FormMixin
from .models import Service, Car, Order
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import (OrderCommentForm,
                    CarCommentForm,
                    UserChangeForm,
                    ProfileChangeForm,
                    OrderCreateUpdateForm)

def index(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'services': Service.objects.count(),
        'cars': Car.objects.count(),
        'orders_done': Order.objects.filter(status='c').count(),
        'num_visits': num_visits,
    }
    return render(request, template_name="index.html", context=context)

def cars(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, per_page=20)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    context = {
        'cars': paged_cars,
    }
    return render(request, template_name="cars.html", context=context)


def car(request, car_pk):
    form = CarCommentForm(request.POST or None)
    car = Car.objects.get(pk=car_pk)
    if form.is_valid():
        form.instance.author = request.user
        form.instance.car = car
        form.save()
        return redirect(reverse("car", kwargs={"car_pk": car_pk}))
    context = {
        'car': car,
        'form': form,
    }
    return render(request, template_name="car.html", context=context)


class OrderListView(generic.ListView):
    model = Order
    template_name = "orders.html"
    context_object_name = "orders"
    paginate_by = 5


class OrderDetailView(FormMixin, generic.DetailView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'
    form_class = OrderCommentForm

    def get_success_url(self):
        return reverse("order", kwargs={"pk": self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.order = self.get_object()
        form.save()
        return super().form_valid(form)


def search(request):
    query = request.GET.get('query')
    context = {
        'query': query,
        'cars': Car.objects.filter(Q(make__icontains=query) |
                                   Q(model__icontains=query) |
                                   Q(license_plate__icontains=query) |
                                   Q(vin_code__icontains=query) |
                                   Q(client_name__icontains=query))
    }
    return render(request, template_name="search.html", context=context)

class UserOrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = "user_orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(client=self.request.user)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")

@login_required
def profile(request):
    u_form = UserChangeForm(request.POST or None, instance=request.user)
    p_form = ProfileChangeForm(request.POST or None, request.FILES, instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        return redirect("profile")
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, template_name="profile.html", context=context)


class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    template_name = "order_form.html"
    form_class = OrderCreateUpdateForm
    success_url = reverse_lazy("user_orders")

    def form_valid(self, form):
        form.instance.client = self.request.user
        form.save()
        return super().form_valid(form)


class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Order
    template_name = "order_form.html"
    form_class = OrderCreateUpdateForm

    def get_success_url(self):
        return reverse("order", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.get_object().client == self.request.user


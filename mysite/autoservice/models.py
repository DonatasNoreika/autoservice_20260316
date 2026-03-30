from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Service(models.Model):
    name = models.CharField(verbose_name="Pavadinimas")
    price = models.DecimalField(verbose_name="Kaina", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.CharField()
    model = models.CharField()
    license_plate = models.CharField()
    vin_code = models.CharField()
    client_name = models.CharField()
    photo = models.ImageField(upload_to="cars", null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"


class Order(models.Model):
    car = models.ForeignKey(to="Car",
                            on_delete=models.SET_NULL,
                            null=True, blank=True,
                            related_name="orders")
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    STATUS_CHOICES = [
        ('a', 'Administered'),
        ('k', 'Cancelled'),
        ('i', 'In Progress'),
        ('c', 'Completed'),
    ]

    status = models.CharField(choices=STATUS_CHOICES, default='a')
    client = models.ForeignKey(to=User,
                               on_delete=models.SET_NULL,
                               null=True, blank=True)

    def is_overdue(self):
        return self.deadline < timezone.now()

    def total(self):
        return sum(line.line_sum() for line in self.lines.all())

    def __str__(self):
        return f"{self.car} - {self.date}"


class OrderLine(models.Model):
    order = models.ForeignKey(to="Order", on_delete=models.CASCADE, related_name='lines')
    service = models.ForeignKey(to="Service", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def line_sum(self):
        return round(self.service.price * self.quantity)

    def __str__(self):
        return f"{self.service} ({self.service.price}) * {self.quantity} = {self.line_sum()}"


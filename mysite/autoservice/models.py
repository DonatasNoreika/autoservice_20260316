from django.db import models


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

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"


class Order(models.Model):
    car = models.ForeignKey(to="Car", on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car} - {self.date}"


class OrderLine(models.Model):
    order = models.ForeignKey(to="Order", on_delete=models.CASCADE)
    service = models.ForeignKey(to="Service", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.service} - {self.quantity}"

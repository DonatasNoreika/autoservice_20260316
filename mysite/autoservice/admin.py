from django.contrib import admin
from .models import Service, Car, Order, OrderLine

class OrderAdmin(admin.ModelAdmin):
    list_display = ['car', 'date']

admin.site.register(Service)
admin.site.register(Car)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)

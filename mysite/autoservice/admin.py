from django.contrib import admin
from .models import Service, Car, Order, OrderLine

class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0
    readonly_fields = ['line_sum']
    fields = ['service', 'quantity', 'line_sum']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['car', 'client', 'date', 'deadline', 'total', 'status']
    inlines = [OrderLineInLine]
    readonly_fields = ['date', 'total']
    list_editable = ['client', 'deadline', 'status']

    fieldsets = [
        ('General', {'fields': ('car', 'client', 'date', 'deadline', 'total', 'status')}),
    ]


class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'license_plate', 'vin_code', 'client_name']
    list_filter = ['make', 'model', 'client_name']
    search_fields = ['license_plate', 'vin_code']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ['order', 'service', 'service__price', 'quantity', 'line_sum']

admin.site.register(Service, ServiceAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)

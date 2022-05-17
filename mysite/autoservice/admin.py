from django.contrib import admin
from .models import Model, Car, Order, OrderLine, Service

admin.site.register(Model)
admin.site.register(Car)
admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(Service)
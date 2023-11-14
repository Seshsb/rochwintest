from django.contrib import admin
from .models import Employee, Client, Order, OrderM2M, Product

admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderM2M)

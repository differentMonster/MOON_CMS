from django.contrib import admin
from .models import CartModel, OrderModel
# Register your models here.
admin.site.register(CartModel)
admin.site.register(OrderModel)

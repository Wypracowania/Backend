from django.contrib import admin
from user.models import Order, OrderInfo
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderInfo)
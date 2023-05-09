from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from order.models import Order, OrderDetail


@register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','is_paid']


@register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order','product','count']
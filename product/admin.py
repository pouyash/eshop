from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from product.models import Product, Category, Brand, ProductVisit


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']

@register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']

@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','is_active','price']


@register(ProductVisit)
class ProductVisitAdmin(admin.ModelAdmin):
    pass
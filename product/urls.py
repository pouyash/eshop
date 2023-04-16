from django.urls import path

from product import views

urlpatterns = [
    path('',views.products,name='products'),
    path('detail/<slug>', views.product_detail, name='product_detail'),
]

from django.urls import path

from product import views

urlpatterns = [
    path('',views.ProductView.as_view(),name='products'),
    path('cat/<slug>', views.ProductView.as_view(), name='product_by_cat'),
    path('brand/<brand_slug>', views.ProductView.as_view(), name='product_by_brand'),
    path('detail/<slug:slug>', views.ProductDetail.as_view(), name='product_detail'),
    path('detail-add/', views.add_session, name='add_session'),
]

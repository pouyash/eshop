from django.urls import path

from order import views

urlpatterns = [
    path('add-to-order/',views.add_to_order,name='add-to-order'),
    path('basket/',views.basket,name='basket'),
    path('remove_basket/', views.remove_basket, name='remove_basket'),
    path('decrease/', views.decrease, name='decrease'),
    path('increase/', views.increase, name='increase'),

    path('request/', views.send_request, name='request'),
    path('verify/', views.verify, name='verify'),
]
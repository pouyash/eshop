from django.urls import path

from contact_us import views

urlpatterns = [
    path('',views.index,name='contact_us')
]
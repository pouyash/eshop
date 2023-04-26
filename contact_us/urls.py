from django.urls import path

from contact_us import views

urlpatterns = [
    path('',views.ContactUsCreateForm.as_view(),name='contact_us'),
    path('profile/', views.ProfileCreateForm.as_view(), name='profile'),
    path('profile-list/', views.ProfileList.as_view(), name='profile-list'),
    path('about-us/', views.AboutUs.as_view(), name='about-us'),
]
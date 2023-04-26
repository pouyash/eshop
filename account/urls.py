from django.urls import path

from account import views

urlpatterns = [
    path('register/',views.Register.as_view(),name='register_page'),
    path('login/', views.Login.as_view(), name='login_page'),
    path('forgot_password/', views.ForgotPassword.as_view(), name='forgot_password'),
    path('reset_password/<code>', views.ResetPassword.as_view(), name='reset_password'),
    path('active/<code>', views.ActivateEmail.as_view(), name='activate'),
    path('logout/', views.log_out, name='logout'),
]

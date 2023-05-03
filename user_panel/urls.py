from django.urls import path

from user_panel import views

urlpatterns = [
    path('',views.index, name='user_panel_home'),
    path('edit_user/', views.EditUser.as_view(), name='user_panel_edit'),
    path('edit_user_password/', views.ChangePassword.as_view(), name='user_panel_password'),
]
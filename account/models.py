from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    email_active_code = models.CharField(max_length=100,verbose_name='کد فعالسازی ایمیل')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'



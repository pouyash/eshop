from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    email_active_code = models.CharField(max_length=100,verbose_name='کد فعالسازی ایمیل')
    avatar = models.ImageField(upload_to='avatar',null=True,blank=True,verbose_name='عکس پروفایل')
    about_user = models.TextField(null=True,blank=True,verbose_name='درباره کاربر')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.username


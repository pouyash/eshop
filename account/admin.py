from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from account.models import User


@register(User)
class UserAdmin(admin.ModelAdmin):
    pass
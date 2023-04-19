from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from contact_us.models import ContactUs, Profile


@register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','subject','email','is_response']



@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
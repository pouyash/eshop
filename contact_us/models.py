from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()
    is_response = models.BooleanField(default=False)
    response = models.TextField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ارتباط با ما'
        verbose_name_plural = 'ارتباط با ما'
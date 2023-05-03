from django.db import models

# Create your models here.

class SiteSettingModel(models.Model):
    site_url = models.CharField(max_length=200,verbose_name='دامنه سایت')
    site_name = models.CharField(max_length=20,verbose_name='نام سایت')
    address = models.CharField(max_length=300,verbose_name='آدرس')
    phone = models.CharField(max_length=20,verbose_name='تلفن',null=True,blank=True)
    email = models.CharField(max_length=20,verbose_name='ایمیل',null=True,blank=True)
    fax = models.CharField(max_length=20,verbose_name='فکس',null=True,blank=True)
    about_us = models.TextField(verbose_name='درباره ما')
    copy_right = models.TextField(verbose_name='قوانین کپی رایت')
    site_logo = models.ImageField(upload_to='images/site_setting/')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name


class FooterBox(models.Model):
    title = models.CharField(max_length=200,verbose_name='عنوان')
    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200,verbose_name='عنوان')
    url = models.CharField(max_length=500)

    footerbox = models.ForeignKey(FooterBox , on_delete=models.CASCADE,related_name='footerlink')

    def __str__(self):
        return self.title



class Slider(models.Model):
    title = models.CharField(max_length=200,verbose_name='عنوان')
    url = models.URLField(max_length=400,verbose_name='لینک')
    url_title = models.CharField(max_length=400,verbose_name='عنوان لینک')
    image = models.ImageField(upload_to='image/slider/')
    description = models.TextField(verbose_name='توضیحات')
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.title


class SiteBanner(models.Model):
    class SiteBannerPosition(models.TextChoices):
        product_list = 'product_list','صفحه لیست محصولات'
        product_detail='product_detail','صفحه جزئیات محصولات'
        about_us = 'about_us','صفحه درباره ما'


    title = models.CharField(max_length=200,verbose_name='عنوان')
    url = models.CharField(max_length=600,null=True,blank=True,verbose_name='لینک')
    image = models.ImageField(upload_to='images/banners',verbose_name='تصویر')
    position = models.CharField(max_length=600,verbose_name='پوزیشن',choices=SiteBannerPosition.choices)
    is_active = models.BooleanField(default=True,verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنرهای تبلیغاتی'
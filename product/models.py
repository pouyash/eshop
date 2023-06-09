from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
# Create your models here.
from django.urls import reverse
from django.utils.text import slugify

from account.models import User


class ValidManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Category(models.Model):
    title = models.CharField(max_length=300,verbose_name='عنوان')
    slug = models.SlugField(null=True,blank=True,verbose_name='عنوان در لینک')
    is_active = models.BooleanField(default=True,verbose_name='فعال/غیرفال')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class Brand(models.Model):
    title = models.CharField(max_length=300,verbose_name='عنوان')
    slug = models.SlugField(null=True, blank=True, verbose_name='عنوان در لینک')
    is_active = models.BooleanField(default=True,verbose_name='فعال/غیرفال')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

class Product(models.Model):
    title = models.CharField(max_length=300,verbose_name='عنوان')
    price = models.IntegerField(verbose_name='قیمت')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='product',null=True,blank=True,verbose_name='دسته بندی')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='product',null=True,blank=True,verbose_name='برند')
    image = models.ImageField(upload_to='product',verbose_name='تصویر محصول',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    short_description = models.CharField(max_length=400)
    rate = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    slug = models.SlugField(default="",null=True,db_index=True,unique=True)
    # image=models.ImageField(upload_to='product')

    objects=models.Manager()
    objects_active=ValidManager()

    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصولات'

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     self.slug = slugify(self.title)
    #     super(Product, self).save()

    def __str__(self):
        return f'{self.title}=>{self.price}'

    def get_absolute_url(self):
        return reverse('product-detail',args=[self.slug])


class ProductVisit(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول',related_name='product_visit')
    ip = models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')

    def __str__(self):
        return f'{self.product.title} / {self.ip}'

    class Meta:
        verbose_name = 'بازدید محصولات'
        verbose_name_plural = 'بازدید محصولات'

class ProductGallery(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    image = models.ImageField(upload_to='images/gallery')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'گالری تصاویر'
        verbose_name_plural = 'گالری تصاویر'

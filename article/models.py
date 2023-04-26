from django.db import models


# Create your models here.
# from jalali_date import datetime2jalali, date2jalali

from account.models import User


class ArticleCategoryModel(models.Model):
    parent = models.ForeignKey('ArticleCategoryModel',on_delete=models.CASCADE,verbose_name='دسته بندی والد',null=True,blank=True)
    title = models.CharField(max_length=200,verbose_name='عنوان')
    title_url = models.CharField(max_length=300,unique=True,verbose_name='عنوان در لینک')
    is_active = models.BooleanField(default=True,verbose_name='فعال / غیرفعال')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقالات'
        verbose_name_plural = 'دسته بندی های مقالات'

class Article(models.Model):
    title = models.CharField(max_length=300,verbose_name='عنوان')
    slug = models.SlugField(max_length=400,db_index=True,unique=True,allow_unicode=True,verbose_name='عنوان در url')
    image = models.ImageField(upload_to='images/article/',verbose_name='تصویر مقاله')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    is_active = models.BooleanField(verbose_name='حالت فعال / غیرفعال')
    categories = models.ManyToManyField(ArticleCategoryModel, verbose_name='دسته بندی ها')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='article',null=True,blank=True,editable=False)

    def __str__(self):
        return self.title

    # def get_jalali_data(self):
    #     return datetime2jalali(self.created_at)
    #
    # def get_jalali_data1(self):
    #     return self.get_jalali_data().strftime("%M:%H")
    # def get_jalali_time(self):
    #     return date2jalali(self.created_at)
    #
    # def get_jalali_time(self):
    #     return self.get_jalali_data().strftime("%H:%M")

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,verbose_name='مقاله',related_name='article')
    parent = models.ForeignKey('ArticleComment',on_delete=models.CASCADE,verbose_name='والد',related_name='parent_comment',null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name='متن کامنت')

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنتها'

    def __str__(self):
        return self.user.get_full_name()

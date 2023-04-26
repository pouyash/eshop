from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from article.models import Article, ArticleCategoryModel


@register(ArticleCategoryModel)
class ArticleCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_url', 'parent', 'is_active']
    list_editable = ['parent', 'is_active']


@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'short_description', 'is_active']
    list_editable = ['slug', 'is_active', 'short_description']




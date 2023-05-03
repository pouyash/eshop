from django.contrib import admin

# Register your models here.
from django.contrib.admin import register
from django.http import HttpRequest

from article.models import Article, ArticleCategoryModel, ArticleComment


@register(ArticleCategoryModel)
class ArticleCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'title_url', 'parent', 'is_active']
    list_editable = ['parent', 'is_active']


@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'short_description', 'is_active','author']
    list_editable = ['slug', 'is_active', 'short_description']

    def save_model(self, request:HttpRequest, obj:Article, form, change):
        obj.author = request.user
        return super(ArticleAdmin, self).save_model(request, obj, form, change)



@register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['user','article','parent']


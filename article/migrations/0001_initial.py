# Generated by Django 4.2 on 2023-04-26 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('slug', models.SlugField(allow_unicode=True, max_length=400, unique=True, verbose_name='عنوان در url')),
                ('image', models.ImageField(upload_to='images/article/', verbose_name='تصویر مقاله')),
                ('short_description', models.TextField(verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('is_active', models.BooleanField(verbose_name='حالت فعال / غیرفعال')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(verbose_name='متن کامنت')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to='article.article', verbose_name='مقاله')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_comment', to='article.articlecomment', verbose_name='والد')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنتها',
            },
        ),
        migrations.CreateModel(
            name='ArticleCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('title_url', models.CharField(max_length=300, unique=True, verbose_name='عنوان در لینک')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.articlecategorymodel', verbose_name='دسته بندی والد')),
            ],
            options={
                'verbose_name': 'دسته بندی مقالات',
                'verbose_name_plural': 'دسته بندی های مقالات',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='article.articlecategorymodel', verbose_name='دسته بندی ها'),
        ),
    ]

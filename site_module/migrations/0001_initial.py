# Generated by Django 4.2 on 2023-04-24 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
            ],
        ),
        migrations.CreateModel(
            name='SiteBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.CharField(blank=True, max_length=600, null=True, verbose_name='لینک')),
                ('image', models.ImageField(upload_to='images/banners', verbose_name='تصویر')),
                ('position', models.CharField(choices=[('product_list', 'صفحه لیست محصولات'), ('product_detail', 'صفحه جزئیات محصولات'), ('about_us', 'صفحه درباره ما')], max_length=600, verbose_name='پوزیشن')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
            ],
            options={
                'verbose_name': 'بنر تبلیغاتی',
                'verbose_name_plural': 'بنرهای تبلیغاتی',
            },
        ),
        migrations.CreateModel(
            name='SiteSettingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_url', models.CharField(max_length=200, verbose_name='دامنه سایت')),
                ('site_name', models.CharField(max_length=20, verbose_name='نام سایت')),
                ('address', models.CharField(max_length=300, verbose_name='آدرس')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='تلفن')),
                ('email', models.CharField(blank=True, max_length=20, null=True, verbose_name='ایمیل')),
                ('fax', models.CharField(blank=True, max_length=20, null=True, verbose_name='فکس')),
                ('about_us', models.TextField(verbose_name='درباره ما')),
                ('copy_right', models.TextField(verbose_name='قوانین کپی رایت')),
                ('site_logo', models.ImageField(upload_to='images/site_setting/')),
                ('is_main_setting', models.BooleanField(verbose_name='تنظیمات اصلی')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.URLField(max_length=400, verbose_name='لینک')),
                ('url_title', models.CharField(max_length=400, verbose_name='عنوان لینک')),
                ('image', models.ImageField(upload_to='image/slider/')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدرها',
            },
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.CharField(max_length=500)),
                ('footerbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='footerlink', to='site_module.footerbox')),
            ],
        ),
    ]

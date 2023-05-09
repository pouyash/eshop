from django.db.models import Count, Sum
from django.shortcuts import render
from utils.convertors import convert_to_group
# Create your views here.
from product.models import Product, Category
from site_module.models import SiteSettingModel, FooterLink, FooterBox, Slider


def home(request):
    slider = Slider.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True).order_by('-id')[:12]
    products_most_viewed = Product.objects.filter(is_active=True).annotate(visit=Count('product_visit')).order_by('-visit')[:12]
    categories = list(Category.objects.annotate(product_count=Count('product')).filter(is_active=True,product_count__gt=0)[:6])
    categories_product = []
    for category in categories:
        item = {
            'id':category.id,
            'title':category.title,
            'products': list(category.product.all())
        }
        categories_product.append(item)
    most_bought_products = Product.objects.filter(order_detail__order__is_paid=True).annotate(order_count=Sum('order_detail__count')).order_by('-order_count')[:12]
    most_bought_products = convert_to_group(most_bought_products)
    context = {
        'sliders':slider,
        'products' : convert_to_group(products),
        'products_most_viewed': convert_to_group(products_most_viewed),
        'categories_product':categories_product,
        'most_bought_products':most_bought_products,
    }
    return render(request,'home/home.html',context)

def header_component(request):
    site = SiteSettingModel.objects.filter(is_main_setting=True).first()
    context = {
        'site':site
    }
    return render(request,'header_component.html',context)


def footer_component(request):
    site = SiteSettingModel.objects.filter(is_main_setting=True).first()
    footer = FooterBox.objects.all()
    context = {
        'site':site,
        'footer':footer
    }
    return render(request,'footer_component.html',context)
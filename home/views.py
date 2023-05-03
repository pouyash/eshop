from django.db.models import Count
from django.shortcuts import render
from utils.convertors import convert_to_group
# Create your views here.
from product.models import Product
from site_module.models import SiteSettingModel, FooterLink, FooterBox, Slider


def home(request):
    slider = Slider.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True).order_by('-id')[:12]
    products_most_viewed = Product.objects.filter(is_active=True).annotate(visit=Count('product_visit')).order_by('-visit')[:12]
    context = {
        'sliders':slider,
        'products' : convert_to_group(products),
        'products_most_viewed': convert_to_group(products_most_viewed),
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
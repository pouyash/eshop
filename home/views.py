from django.shortcuts import render

# Create your views here.
from site_module.models import SiteSettingModel, FooterLink, FooterBox, Slider


def home(request):
    slider = Slider.objects.filter(is_active=True)
    context = {
        'sliders':slider
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
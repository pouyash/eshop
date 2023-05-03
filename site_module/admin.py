from django.contrib import admin
from django.contrib.admin import register

from site_module.models import SiteSettingModel, FooterBox, FooterLink, Slider, SiteBanner


@register(SiteSettingModel)
class SiteSettingModelAdmin(admin.ModelAdmin):
    pass

@register(FooterBox)
class FooterBoxAdmin(admin.ModelAdmin):
    pass

@register(FooterLink)
class FooterLinkModelAdmin(admin.ModelAdmin):
    pass


@register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass
@register(SiteBanner)
class SiteBannerAdmin(admin.ModelAdmin):
    pass
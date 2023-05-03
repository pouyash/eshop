from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from sweetify import sweetify

from article.models import ArticleCategoryModel
from product.models import Product, Category, Brand, ProductVisit
from django.views.generic import ListView, DetailView

from site_module.models import SiteBanner
from utils.http_services import get_ip_address

class ProductView(ListView):
    template_name = 'product/products.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductView, self).get_context_data()
        product = Product.objects.order_by('-price').first().price
        context['db_max_price'] = product
        context['start_price'] = 0
        context['end_price'] = product
        context['banners'] = SiteBanner.objects.filter(is_active=True,position=SiteBanner.SiteBannerPosition.product_list)
        return context
    def get_queryset(self):
        q = super(ProductView, self).get_queryset()
        q = q.filter(is_active=True)
        slug = self.kwargs.get('slug')

        start_price = self.request.GET.get('start_price')
        end_price = self.request.GET.get('end_price')
        if start_price is not None:
            q = q.filter(price__gte=start_price)

        if end_price is not None:
            q = q.filter(price__lte=end_price)

        if slug is not None:
            q = q.filter(category__slug__iexact=slug)
        brand_slug = self.kwargs.get('brand_slug')
        if brand_slug is not None:
            q = q.filter(brand__slug__iexact=brand_slug)
        return q


class ProductDetail(DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    context_object_name = 'product'

    def get_queryset(self):
        q = super(ProductDetail, self).get_queryset()
        q = q.filter(is_active=True)
        return q

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        product = self.object.slug
        # context['is_favorite'] = self.request.session.get('favorite') == product
        context['is_favorite'] = self.request.COOKIES.get('favorite') == product
        ip_address =get_ip_address(self.request)
        product_visited = ProductVisit.objects.filter(ip__iexact=ip_address,product_id=self.object.id).exists()
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user
        if not product_visited :
            ProductVisit.objects.create(user=user,ip=ip_address,product_id=self.object.id)

        return context


def add_session(request):
    slug = request.POST.get('product_slug')
    product= Product.objects.get(slug=slug)
    # request.session['favorite'] = product.slug
    response = redirect(reverse('product_detail',args={slug:slug}))
    expires = 7 * 24 * 60*60
    response.set_cookie('favorite',product.slug,expires=expires)
    return response



def right_sidbar_component(request):
    categories = Category.objects.filter(is_active=True)
    brands = Brand.objects.filter(is_active=True).annotate(count=Count('product'))
    context = {
        'categories':categories,
        'brands':brands
    }
    return render(request,'product/right_sidbar.html',context)
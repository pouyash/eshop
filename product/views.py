from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from sweetify import sweetify


from product.models import Product
from django.views.generic import ListView, DetailView


class ProductView(ListView):
    template_name = 'product/products.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1

    def get_queryset(self):
        q = super(ProductView, self).get_queryset()
        q= q.filter(is_active=True)
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
    return render(request,'product/right_sidbar.html',{})
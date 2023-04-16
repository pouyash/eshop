from django.db.models import Avg, Min
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from product.models import Product


def products(request):
    products = Product.objects.all()
    return render(request,'product/products.html',context=
    {
        'products':products,
     })

def product_detail(request,slug):
    product = get_object_or_404(Product,slug=slug)
    return render(request,'product/product_detail.html',context={'product':product})





def right_sidbar_component(request):
    return render(request,'product/right_sidbar.html',{})
import datetime
from datetime import time
import time

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render,redirect
import requests
import json
# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse

from order.models import Order, OrderDetail
from product.models import Product

@login_required(login_url='login_page')
def add_to_order(request):
    product_id = request.GET.get('productId')
    count = request.GET.get('count')
    if int(count) < 1:
        return JsonResponse({
            'status': 'error',
            'text': 'تعداد محصولات نامعتبر است',
            'icon': 'success',
            'button': 'Ok',
        })
    if request.user.is_authenticated:
        product = Product.objects.filter(is_active=True, id=product_id).first()
        if product is not None:
            order, create = Order.objects.get_or_create(user_id=request.user.id, is_paid=False)
            order_detail = OrderDetail.objects.filter(order=order, product_id=product_id).first()
            if order_detail is not None:
                order_detail.count += int(count)
                order_detail.save()
            else:
                order_detail = OrderDetail(product_id=product_id, count=int(count), order=order)
                order_detail.save()
            return JsonResponse({
                'status': 'success',
                'text': 'با موفقیت به سبد خرید افزوده شد',
                'icon': 'success',
                'button': 'Ok',
            })
        else:
            return JsonResponse({
                'status': 'not_found',
                'text': 'محصول مورد نظر یافت نشد',
                'icon': 'warning',
                'button': 'امتحان دوباره',
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'لطفا وارد سایت شوید',
            'icon': 'warning',
            'button': 'وارد شوید',
        })

@login_required(login_url='login_page')
def basket(request):
    order,created = Order.objects.get_or_create(is_paid=False,user=request.user)
    order_detail = order.order_detail.all()
    sum = order.get_total()
    context = {
        'order_detail':order_detail,
        'sum':sum,
    }
    return render(request,'order/basket_content.html',context)
@login_required(login_url='login_page')
def remove_basket(request):
    detail_id = request.GET.get('id')
    order_detail:OrderDetail = OrderDetail.objects.filter(id=detail_id).first()
    if order_detail:
        order_detail.delete()

    order = Order.objects.prefetch_related('order_detail').filter(is_paid=False,user=request.user).first()
    order_detail = order.order_detail.all()
    sum = order.get_total()

    context = {
        'order_detail':order_detail,
        'sum':sum,
    }
    data = render_to_string('order/basket.html',context,request=request)
    return JsonResponse({
        'text':'با موفقیت حذف شد',
        'icon':'success',
        'button':'success',
        'status': 'ok',
        'body': data,
    })
@login_required(login_url='login_page')
def decrease(request):
    detail_id = request.GET.get('id')
    order_detail: OrderDetail = OrderDetail.objects.filter(id=detail_id).first()
    if order_detail:
        if order_detail.count == 1:
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()

    order = Order.objects.prefetch_related('order_detail').filter(is_paid=False, user=request.user).first()
    order_detail = order.order_detail.all()
    sum = 0
    for order in order_detail:
        sum += order.product.price * order.count

    context = {
        'order_detail': order_detail,
        'sum': sum,
    }
    data = render_to_string('order/basket.html', context, request=request)
    return JsonResponse({
        'text':'با موفقیت کم شد',
        'icon':'success',
        'button':'success',
        'status': 'ok',
        'body': data,
    })
@login_required(login_url='login_page')
def increase(request):
    detail_id = request.GET.get('id')
    order_detail: OrderDetail = OrderDetail.objects.filter(id=detail_id).first()
    if order_detail:
        order_detail.count += 1
        order_detail.save()

    order = Order.objects.prefetch_related('order_detail').filter(is_paid=False, user=request.user).first()
    order_detail = order.order_detail.all()
    sum = 0
    for order in order_detail:
        sum += order.product.price * order.count

    context = {
        'order_detail': order_detail,
        'sum': sum,
    }
    data = render_to_string('order/basket.html', context, request=request)
    return JsonResponse({
        'text':'با موفقیت افزوده شد',
        'icon':'success',
        'button':'success',
        'status': 'ok',
        'body': data,
    })



sandbox = 'sandbox'
MERCHANT = "00000000-0000-0000-0000-000000000000"
ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
CallbackURL = 'http://127.0.0.1:8000/order/verify/'
@login_required(login_url='login_page')
def send_request(request:HttpRequest):
    user_basket,created = Order.objects.get_or_create(is_paid=False,user=request.user)
    try:
        amount = user_basket.get_total()
    except:
        return redirect(reverse('basket'))

    data = {
        "MerchantID": MERCHANT,
        "Amount": amount,
        'Description':description,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)
        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                try:
                    return redirect(ZP_API_STARTPAY + str(response['Authority']),
                                    {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),
                                     'authority': response['Authority']})
                except:
                    return HttpResponse('FUCK YOU')
            else:
                return {'status': False, 'code': str(response['Status'])}
        return redirect(reverse('basket'))

    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}

@login_required(login_url='login_page')
def verify(request:HttpRequest):
    authority = request.GET.get('Authority')
    user_basket,created = Order.objects.get_or_create(is_paid=False,user=request.user)
    try:
        amount = user_basket.get_total()
    except:
        return redirect(reverse('basket'))
    data = {
        "MerchantID": MERCHANT,
        "Amount": amount,
        "Authority": authority,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            user_basket.is_paid=True
            user_basket.payment_date = datetime.datetime.now()
            user_basket.save()
            return redirect(reverse('basket'))
        else:
            return redirect(reverse('basket'))
    return redirect(reverse('basket'))
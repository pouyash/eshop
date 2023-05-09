from django.db import models

from account.models import User
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='کاربر',related_name='order')
    is_paid = models.BooleanField(verbose_name='پرداخت شده/نشده')
    payment_date = models.DateTimeField(null=True,blank=True,verbose_name='تاریخ پرداخت')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total(self):
        total = 0
        if self.is_paid == False:
            for od in self.order_detail.all():
                total += od.product.price * od.count
        else:
            for od in self.order_detail.all():
                total += od.final_price * od.count
        return total

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_detail',verbose_name='سفارش')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_detail',verbose_name='محصول')
    final_price = models.IntegerField(null=True,blank=True,verbose_name='قیمت نهایی')
    count = models.IntegerField(verbose_name='تعداد')

    def get_total_price(self):
        return self.count * self.product.price

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'جزئیات سفارشات'
        verbose_name_plural = 'جزئیات سفارشات'

    def save(self,*args,**kwargs):
        self.final_price = self.product.price * self.count
        super(OrderDetail, self).save(*args,**kwargs)


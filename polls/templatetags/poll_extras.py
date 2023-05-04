import jalali_date
from django import template

register = template.Library()

@register.filter(name='to_jalali')
def to_jalali(value):
    return jalali_date.date2jalali(value)

@register.filter(name='to_jalali_time')
def to_jalali_time(value):
    return jalali_date.datetime2jalali(value).strftime('%H:%M:%S')

@register.filter('three_digit_currency')
def three_digit_currency(value):
    return '{:,}'.format(value)


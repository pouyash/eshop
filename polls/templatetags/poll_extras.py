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

@register.simple_tag
def multiply(val1,val2):
    return three_digit_currency(val1*val2)
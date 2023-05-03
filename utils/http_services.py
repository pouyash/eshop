from django.http import HttpRequest


def get_ip_address(request:HttpRequest):
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip is not None:
        add = ip.split(',')[0]
    else:
        add = request.META.get("REMOTE_ADDR")
    return add
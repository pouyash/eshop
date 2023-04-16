from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home/home.html')

def header_component(request):
    return render(request,'header_component.html',{})


def footer_component(request):
    return render(request,'footer_component.html',{})
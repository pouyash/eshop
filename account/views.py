import datetime
import sweetify
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpRequest
from django.urls import reverse
from django.utils.crypto import get_random_string

from account.models import User
from django.shortcuts import render,redirect
from django.views import View

from account.forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from utils.email import send_email


class Register(View):
    def get(self,request):
        form = RegisterForm()

        return render(request,'account/register.html',context={'form':form})

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.filter(email__iexact=email).exists()
            if user:
                form.add_error('email','ایمیل قبلا ثبت شده است')
            else:
                user = User(email=email,email_active_code=get_random_string(72)+str(datetime.datetime.now()))
                user.set_password(form.cleaned_data.get('password'))
                user.is_active=False
                user.username = email
                user.save()
                send_email('فعالسازی اکانت کاربر', to=user.email, context={'user': user}, template='emails/active.html')
                sweetify.success(request,'ایمیل با موفقیت ارسال شد لطفتا ایمیلتان را تایید کنید')
                return redirect(reverse('login_page'))
        return render(request,'account/register.html',context={'form':form})



class Login(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        form = LoginForm()
        return render(request,'account/login.html',context={'form':form})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=email).first()
            if user is not None:
                check_pass = user.check_password(password)
                if user.is_active == True and check_pass:
                    login(request,user)
                    sweetify.success(request,'با موفقیت وارد شدید')
                    return redirect(reverse('home'))
                else:
                    form.add_error('email','ایمیل نامعتبر است یا رمز عبور نادرست میباشد.')
            else:
                form.add_error('email','ایمیل نامعتبر است یا رمز عبور نادرست میباشد.')
        return render(request,'account/login.html',context={'form':form})



class ActivateEmail(View):
    def get(self,request,code):
        user = User.objects.filter(email_active_code__iexact=code).first()
        if user is not None:
            if not user.is_active:
                user.is_active=True
                user.email_active_code = get_random_string(72) + str(datetime.datetime.now())
                user.save()
                return redirect(reverse('login_page'))
            else:
                pass
        else:
            raise Http404



class ForgotPassword(View):
    def get(self,request):
        form = ForgotPasswordForm()
        return render(request,'account/forgot_password.html',context={'form':form})

    def post(self,request:HttpRequest):
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.filter(email__iexact=email).first()
            if user is not None:
                user.email_active_code = get_random_string(72) + str(datetime.datetime.now())
                user.save()
                sweetify.success(request,'با موفقیت ایمیل ارسال شد. لطفا ایمیلتان را چک کنید')
                send_email('بازیابی رمز عبور',user.email,context={'user':user},template='emails/forgot.html')
            else:
                form.add_error('email','ایمیل موردنظر یافت نشد!')
        return render(request,'account/forgot_password.html',context={'form':form})


class ResetPassword(View):
    def get(self,request,code):
        form = ResetPasswordForm()
        user = User.objects.filter(email_active_code__iexact=code).first()
        if user is not None:
            context = {
                'form':form,
                'user':user
            }
            return render(request,'account/reset_password.html',context)
        else:
            return redirect(reverse('login_page'))
    def post(self,request,code):
        form = ResetPasswordForm(request.POST)
        user = User.objects.filter(email_active_code__iexact=code).first()
        if user is not None:
            if form.is_valid():
                user.is_active=True
                user.email_active_code = get_random_string(72)+str(datetime.datetime.now())
                user.set_password(form.cleaned_data.get('password'))
                user.save()
                sweetify.success(request,'با موفقیت رمز عبور تغییر یافت')
                return redirect(reverse('login_page'))
            else:
                context = {
                    'form': form,
                    'user': user
                }
                sweetify.error(request,'مشکلی بوجو آمده است')
                return render(request,'account/reset_password.html',context)
        else:
            return redirect(reverse('login_page'))

@login_required(login_url='home')
def log_out(request):
    logout(request)
    sweetify.success(request,'با موفقیت خارج شدید')
    return redirect(reverse('home'))
from audioop import reverse

import sweetify
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from user_panel.forms import UserEditForm, ChangePasswordForm


@login_required(login_url='/login')
def index(request):
    return render(request, 'user_panel/index.html')

@method_decorator(login_required(login_url='/login'), name='dispatch')
class EditUser(View):
    def get(self,request:HttpRequest):
        user = request.user
        form = UserEditForm(instance=user)
        context = {
            'form':form
        }
        return render(request,'user_panel/user_edit.html',context)

    def post(self,request:HttpRequest):
        user = request.user
        form = UserEditForm(request.POST, request.FILES,instance=user)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'ویرایش مشخصات با موفقیت انجام شد')
        else:
            sweetify.error(request, 'مشکلی بوجود آمده است')
        context = {
            'form':form
        }
        return render(request, 'user_panel/user_edit.html', context)

@method_decorator(login_required(login_url='/login'), name='dispatch')
class ChangePassword(View):
    def get(self,request:HttpRequest):
        form = ChangePasswordForm()
        context = {
            'form':form,
        }
        return render(request, 'user_panel/change_password.html',context)

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        user = request.user
        if form.is_valid():
            if user.check_password(form.cleaned_data.get('current_password')):
                user.set_password(form.cleaned_data.get('password'))
                user.save()
                logout(user)
                return redirect(reverse('login_page'))

            else:
                form.add_error('current_password','رمز عبور نادرست است')
        context = {
            'form':form,
        }
        return render(request, 'user_panel/change_password.html',context)

def list_component(request):
    return render(request,'user_panel/list_component.html',{})
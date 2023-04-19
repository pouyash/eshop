
from django.contrib import messages
from django.http import HttpRequest

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView

from contact_us.forms import ContactUs_Forms, PorfileForm
import sweetify
from django.views.generic.edit import FormView,CreateView

from contact_us.models import ContactUs, Profile


# class Index(FormView):
#     template_name = 'contact_us/index.html'
#     form_class = ContactUs_Forms
#     success_url = reverse_lazy('contact_us')
#     def form_valid(self, form):
#         request = self.request
#         sweetify.success(request, 'با موفقیت افزوده شد')
#         form.save()
#         return super(Index, self).form_valid(form)
#     def form_invalid(self, form):
#         request = self.request
#         sweetify.error(request, 'با خطا مواجه شده است')
#         return super(Index, self).form_invalid(form)

class ContactUsCreateForm(CreateView):
    model = ContactUs
    template_name = 'contact_us/index.html'
    form_class = ContactUs_Forms
    success_url = reverse_lazy('contact_us')
    def form_valid(self, form):
        request = self.request
        sweetify.success(request, 'با موفقیت افزوده شد')
        form.save()
        return super(ContactUsCreateForm, self).form_valid(form)
    def form_invalid(self, form):
        request = self.request
        sweetify.error(request, 'با خطا مواجه شده است')
        return super(ContactUsCreateForm, self).form_invalid(form)


class ProfileCreateForm(CreateView):
    model = Profile
    template_name = 'contact_us/profile.html'
    form_class = PorfileForm
    success_url = reverse_lazy('profile-list')

    
    def form_valid(self, form):
        sweetify.success(self.request,'با موفقیت افزوده شد')
        return super(ProfileCreateForm, self).form_valid(form)

    def form_invalid(self, form):
        sweetify.error(self.request,'خطایی بوجود آمده است')
        return super(ProfileCreateForm, self).form_invalid(form)

class ProfileList(ListView):
    model = Profile
    template_name = 'contact_us/profile_list.html'
    context_object_name = 'profiles'
from django import forms

from contact_us.models import ContactUs, Profile


class ContactUs_Forms(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name','email','subject','message']
        required = ['name','email','subject','message']
        labels = {
            'name':'نام و نام خانوادگی',
            'email': 'ایمیل',
            'subject': 'عنوان',
            'message': 'متن پیغام',
        }
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'نام و نام خانوادگی',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@gmail.com',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'موضوع',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id':'message',
            }),
        }
        error_messages = {
            'name':{
                'required':'لطفا نام و نام خانوادگی را پر نمائید با تشکر'
            }
        }

class PorfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

        labels = {
            'image':'تصویر'
        }


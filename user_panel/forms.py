from django import forms
from django.contrib.auth import validators
from django.core import validators
from django.core.exceptions import ValidationError

from account.models import User


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','avatar','address','about_user']
        required = ['first_name','last_name','avatar','address','about_user']

        widgets = {
            'first_name':forms.TextInput(attrs={
                "class":'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                "class": 'form-control'
            }),
            'address': forms.Textarea(attrs={
                "class": 'form-control'
            }),
            'about_user': forms.Textarea(attrs={
                "class": 'form-control'
            }),

        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }),label='رمز عبور فعلی')

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }),label='رمز عبور',validators=[validators.MinLengthValidator(8)])

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }),label='تکرار رمز عبور')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('رمز عبور با تکرار رمز عبور مغایرت دارد')
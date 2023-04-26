from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(label='ایمیل',validators=[validators.MaxLengthValidator(100),validators.MinLengthValidator(10)])
    password = forms.CharField(widget=forms.PasswordInput(),label=' رمز عبور')
    confirm_password = forms.CharField(widget=forms.PasswordInput(),label='تکرار رمز عبور')


    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('رمز عبور با تکرار رمز عبور متفاوت است')


class LoginForm(forms.Form):
    email = forms.EmailField(label='ایمیل',validators=[validators.EmailValidator,validators.MaxLengthValidator(100),validators.MinLengthValidator(10)])
    password = forms.CharField(widget=forms.PasswordInput(),label='رمز عبور')


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='ایمیل')


class ResetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(),label='رمز عبور',validators=[validators.MinLengthValidator(8)])
    confirm_password = forms.CharField(widget=forms.PasswordInput(),label='تکرار رمز عبور')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('رمز عبور با تکرار رمز عبور متفاوت است')
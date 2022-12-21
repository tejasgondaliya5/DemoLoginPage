# pip install django-simple-captcha
from logging import PlaceHolder
from django import forms
from captcha.fields import CaptchaField

class InputForm(forms.Form):
   
    userName = forms.CharField(
    max_length = 200,
    widget=forms.TextInput(attrs={'class': "form-control form-control-sm", 'placeholder': 'hannah.green@test.com'}),
    )
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': "form-control form-control-sm", 'placeholder': 'Password@123'}))
    securityText = CaptchaField()

from django import forms
from phonenumber_field.formfields import PhoneNumberField


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CustomUserRegistrationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phonenumber = PhoneNumberField(region='US')
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

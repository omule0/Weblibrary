from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    names = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Please Enter your full name'
    }))

    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter Email Address'
    }))

    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'At least eight characters'
    }))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Please Confirm Password'
    }))

    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Enter Username'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

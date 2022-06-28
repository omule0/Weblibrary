from . import models
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages

def studentLogin(request):
    return render(request , 'studentLogin.html')

def studentSignup(request):
    return render(request , 'studentSignup.html')



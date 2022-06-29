from urllib import request
from . import models
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages


def studentLogin(request):
    pass

def studentSignup(request):
        #collect data if the request method is POST
    if request.method == "POST":
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        gmail = request.POST['email']
        d_o_b = request.POST['dob']
        password = request.POST['pass']
        #map the data collected to the database
        new_user_account = models.studentSignup(FIRSTNAME=f_name , LASTNAME=l_name , EMAIL=gmail ,PASSWORD=password , DATE_OF_BIRTH=d_o_b)
        #now save the data to the database
        new_user_account.save()
        return redirect('studenthome.html')
    else:
        return render(request , 'studentSignup.html')
        

def studentLogout(request):
    pass

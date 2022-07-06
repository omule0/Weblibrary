from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from . import models


def studentLogin(request):
    if request.method == "POST":
        mail = request.POST['email']
        pword = request.POST['pass']
        l_credentials = authenticate(request, username=mail, password=pword)
        if l_credentials is not None:
            login(request, l_credentials)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'studentLogin.html')


def studentSignup(request):
    if request.method == "POST":
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        mail = request.POST['email']
        dob = request.POST['dob']
        pword = request.POST['pass']
        credentials = models.studentSignup(FIRSTNAME=f_name, LASTNAME=l_name, EMAIL=mail, PASSWORD=pword,
                                           DATE_OF_BIRTH=dob)
        credentials.save()
        # return a message if account creation is successful
        return redirect('home')
    else:
        return render(request, 'studentSignup.html')


def StudentLogout(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect("/")


def studentshome(request):
    return render(request, 'studentshome.html')

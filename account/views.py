from . import models
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages

def Student_Reg(request):
    if request.method == "POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        save_student_details = models.StudentReg(FirstName=fname ,LastName=lname ,mail=email, password=password)
        save_student_details.save()
    return render(request , 'student_reg.html' )


def Student_Login(request):
    if request.method == "GET":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user != None:
            auth.login(request , user)
            return redirect("/")
        else:
            messages.info(request , 'invalid credentials')
            return redirect("student_login")

    
        

    return render(request , 'Student_Login.html')





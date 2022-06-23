from account import models
from django.shortcuts import render
from django.http import HttpResponse

def StudentReg(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        save_student_details = StudentReg(firstname=first_name , lastname=last_name , mail=email , password=password)
        save_student_details.save()
    return render(request , 'student_reg.html' )





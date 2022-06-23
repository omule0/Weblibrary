from . import models
from django.shortcuts import render
from django.http import HttpResponse

def Student_Reg(request):
    if request.method == "POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        save_student_details = models.StudentReg(FirstName=fname ,LastName=lname ,mail=email, password=password)
        save_student_details.save()
    return render(request , 'student_reg.html' )





from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
from django.http import HttpResponse
=======
from .forms import CreateUserForm

>>>>>>> a241849a6292592d7c34c1f1ed0d867b47a4e9dd

def student_signup(request):
    register_form = CreateUserForm()
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Account Created Successfully!")
            return redirect('login')
    return render(request, 'studentSignup.html', {'register_form': register_form})


def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")

<<<<<<< HEAD
def logout(request):
    #logout from any account currently logged in
    pass
=======
    return render(request, 'studentLogin.html', {})


def student_logout(request):
    logout(request)
    return redirect('home')
>>>>>>> a241849a6292592d7c34c1f1ed0d867b47a4e9dd

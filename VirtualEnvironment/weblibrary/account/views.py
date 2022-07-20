from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import CreateUserForm


def student_signup(request):
    register_form = CreateUserForm()
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.info(request, "Account Created Successfully!")
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
            messages.info(request, "Invalid Credentials")

    return render(request, 'studentLogin.html', {})


def student_logout(request):
    logout(request)
    return redirect('home')

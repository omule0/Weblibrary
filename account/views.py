import re
from django.shortcuts import render
from django.http import HttpResponse

#views for the home app
    #view to Create a New Account
    #view to login users
    #view to logout users

def createNewAccount(request):
    singup = render(request , '/')

def login(request):
    #login to student account | librarian account
    pass

def logout(request):
    #logout from any account currently logged in
    pass


































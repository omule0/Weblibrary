from django.shortcuts import render , redirect

<<<<<<< HEAD
# Create your views here.
#views for the home app
    #view to call default landing page or home page
    #view to redirect to student account -> accounts app
    #view to redirect to librarian account -> accounts app

def home(request):
    return render(request , 'home.html')
    #return home page or index page
    #pass

def student_account(request):
    #redirect student to login or account creation
    pass

def librarian_account(request):
    #redirect librarian to login or account creation
    pass
=======

def home(request):
    return render(request, 'home.html')
>>>>>>> a241849a6292592d7c34c1f1ed0d867b47a4e9dd

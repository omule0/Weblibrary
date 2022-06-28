from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def student_account(request):
    pass


def librarian_account(request):
    pass

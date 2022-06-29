from django.urls import path 
from . import views

urlpatterns = [ 
    #login
    path("" , views.studentLogin) ,
    #signup
    path('studentSignup.html' , views.studentSignup),
    
]


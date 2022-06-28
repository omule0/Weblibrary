from django.urls import path 
from . import views

urlpatterns = [ path('' ,views.studentLogin) , path('templates/' , views.studentSignup)]
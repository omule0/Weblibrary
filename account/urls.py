from django.urls import path 
from . import views

urlpatterns = [path('studentreg/', views.StudentReg)]
from django.urls import path 
from . import views

urlpatterns = [path('studentreg/', views.Student_Reg), 
path('studentlogin/' ,views.Student_Login)]
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.studentLogin, name="login"),
    path('signup/', views.studentSignup, name="signup"),
    path('logout/', views.StudentLogout, name="logout"),
    path('home', views.studentshome, name="home"),
]

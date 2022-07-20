from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_login, name="login"),
    path('signup/', views.student_signup, name="signup"),
    path('logout/', views.student_logout, name="logout"),
]

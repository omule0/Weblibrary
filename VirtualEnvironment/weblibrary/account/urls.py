from django.urls import path
from . import views

<<<<<<< HEAD
urlpatterns = [path('' , views.createNewAccount , name= 'create_new_account')]
=======
urlpatterns = [
    path('', views.student_login, name="login"),
    path('signup/', views.student_signup, name="signup"),
    path('logout/', views.student_logout, name="logout"),
]
>>>>>>> a241849a6292592d7c34c1f1ed0d867b47a4e9dd

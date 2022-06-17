from django.urls import path 
from . import views

urlpatterns = [path('' , views.createNewAccount , name= 'create_new_account')]
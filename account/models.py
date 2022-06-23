import email
from multiprocessing import AuthenticationError
from turtle import title
from django.db import models

#model to add book

#model to capture student details during registration
class StudentReg(models.Model):
    firstname =models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    mail = models.EmailField(default="library@email.tld")
    password = models.CharField()
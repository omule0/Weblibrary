from multiprocessing import AuthenticationError
from turtle import title
from django.db import models

#model to capture student details during registration

class StudentReg(models.Model):
    FirstName =models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    mail = models.EmailField(default="library@email.tld")
    password = models.CharField(max_length=255)
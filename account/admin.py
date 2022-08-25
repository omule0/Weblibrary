from django.contrib import admin
from . import models
from .models import studentSignup

admin.site.register(models.studentSignup)
admin.site.unregister(studentSignup)

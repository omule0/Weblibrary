from multiprocessing import AuthenticationError

from django.db import models


# model to capture student details during registration
class studentSignup(models.Model):
    FIRSTNAME = models.CharField(max_length=255)
    LASTNAME = models.CharField(max_length=255)
    EMAIL = models.EmailField(default="citizen0@utopia.com")
    PASSWORD = models.CharField(max_length=255)
    DATE_OF_BIRTH = models.DateField()
    # GENDER = models.BooleanField(default=False)

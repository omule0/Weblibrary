from django.db import models

class Media(models.Model):
    file_upload = models.FileField()

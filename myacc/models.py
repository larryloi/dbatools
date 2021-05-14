from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.

class DeployFilesAdmin(models.Model):
    deployadminupload=models.FileField(upload_to='myacc')

    def __str__(self):
        return str(self.deployadminupload)

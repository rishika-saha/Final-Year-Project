from django.db import models

# Create your models here.

class attendance(models.Model):
    roll=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    mrec=models.IntegerField()
    dt=models.DateTimeField()
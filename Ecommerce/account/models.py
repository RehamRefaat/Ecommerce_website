from django.db import models

# Create your models here.
class Account(models.Model):
    UserName=models.CharField(max_length=50)
    UserPassword=models.CharField(max_length=20)
    UserEmail=models.CharField(max_length=25)
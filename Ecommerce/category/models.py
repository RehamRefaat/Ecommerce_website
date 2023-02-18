from django.db import models

# Create your models here.
class Category(models.Model):
    Idcat = models.AutoField(primary_key=True)
    namecat = models.CharField(max_length=50)

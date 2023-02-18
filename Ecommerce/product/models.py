from django.db import models
# Create your models here.
class Product(models.Model):
    Idpro=models.AutoField(primary_key=True)
    namepro=models.CharField(max_length=50)
    catid=models.ForeignKey('category.Category',on_delete=models.CASCADE,default=1)
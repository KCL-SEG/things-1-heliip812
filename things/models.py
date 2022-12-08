from django.db import models

class Transfer(models.Model):
    """Bank Transfer Model"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    name = models.IntegerField(max_length=30)
    
# Create your models here.

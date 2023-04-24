from django.db import models

# Create your models here.

class Schools(models.Model):
    id:models.AutoField(primary_key=True, blank=False, default='')
    name=models.CharField(max_length=50,blank=False, default='')
    email=models.CharField(max_length=100,blank=False, default='')
    phone=models.CharField(max_length=12,blank=False, default='')
    address=models.CharField(max_length=100,blank=False, default='')

  
from django.db import models
from schools.models import Schools

# Create your models here.

class Users(models.Model):
    id:models.AutoField(primary_key=True, blank=False, default='')
    name=models.CharField(max_length=50,blank=False, default='')
    email=models.CharField(max_length=100,blank=False, default='',unique=True)
    phone=models.CharField(max_length=12,blank=False, default='')
    role=models.CharField(max_length=50,blank=False, default='')
    password=models.CharField(max_length=50,blank=False, default='')
    schoolId = models.ForeignKey(Schools, on_delete=models.CASCADE, blank=True,null=True) 

  
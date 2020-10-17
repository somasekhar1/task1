from django.db import models

# Create your models here.
class AdminRegister(models.Model):
    name=models.CharField(max_length=40)
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=30)

class SbiManager(models.Model):
    manager_name=models.CharField(max_length=40)
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=30)
    location=models.CharField(max_length=40)

class IciciManager(models.Model):
    manager_name=models.CharField(max_length=40)
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=30)
    location=models.CharField(max_length=40)

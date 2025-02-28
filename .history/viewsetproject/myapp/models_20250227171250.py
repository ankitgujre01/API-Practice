from django.db import models

# Create your models here.

class  Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    batch = models.CharField(max_length=50)
    
class Cars(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    color = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    
class Criminal(model.Model):
    name     
from django.db import models


class Student(models.Model):
    roll_number= models.IntegerField(primary_key=True)
    name= models.CharField(max_length=100)
    dept= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    phone= models.CharField(max_length=12)

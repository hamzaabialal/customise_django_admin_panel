from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()


class StudentProfile(models.Model):
    discription = models.TextField()
    full_name = models.CharField(max_length=100)
    permanent_address = models.IntegerField(max_length=100)
    phone_number = models.CharField(max_length=78)

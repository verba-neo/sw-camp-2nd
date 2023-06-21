from django.db import models


class Student(models.Model):
    name    = models.CharField(max_length=30)
    phone   = models.CharField(max_length=15)
    email   = models.EmailField()
    address = models.CharField(max_length=200)
    age     = models.PositiveSmallIntegerField()
    major   = models.CharField(max_length=100)
    year    = models.DateField()
    bio     = models.TextField()


class Reply(models.Model):
    pass

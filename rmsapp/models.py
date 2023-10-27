from django.db import models
from datetime import datetime


# Create your models here.

class usersignup(models.Model):
    created = models.DateTimeField(default=datetime.now(),blank=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=30)
    email=models.EmailField()
    password = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class ryph(models.Model):
    created = models.DateTimeField(default=datetime.now(),blank=True)
    title = models.CharField(max_length=200)
    cate = models.CharField(max_length=200)
    file = models.FileField(upload_to='static/uploded_file/')
    comments = models.TextField()

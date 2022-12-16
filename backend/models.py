from datetime import datetime
from django.db import models

# Create your models here.

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    creatorId = models.IntegerField()
    name = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    description = models.TextField()
    image = models.TextField()
    imageName = models.CharField(max_length=10000000, default = "")
    targetPrice = models.TextField()
    isFeatured = models.BooleanField()
    currentPrice = models.IntegerField(default = 0)
    donationCount = models.IntegerField(default = 0)
    createAt = models.DateTimeField(default=datetime.now)

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    avatar = models.TextField(default = "")
    coverBackground = models.TextField(default = "")
    description = models.TextField(max_length=10000)
    facebook = models.CharField(max_length=500, default = "")
    phone = models.CharField(max_length=20, default = "")
    createAt = models.DateTimeField(default=datetime.now)
    
class Contribution(models.Model):
    id = models.AutoField(primary_key=True)  
    userId = models.IntegerField()
    projectId = models.IntegerField()
    amount = models.IntegerField()
    createAt = models.DateTimeField(default=datetime.now)

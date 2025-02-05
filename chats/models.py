from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=10000)

class Message(models.Model):
    value = models.CharField(max_length=1000)
    date = models.DateField(("Date"), auto_now_add=True)
    room = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)
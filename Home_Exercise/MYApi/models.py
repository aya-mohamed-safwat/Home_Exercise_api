from django.db import models

class Users(models.Model):
    userId  = models.BigAutoField( primary_key=True)
    name    = models.CharField(max_length=100)
    genderType = models.TextChoices('Male', 'Female',)
    gender  = models.CharField(blank=True, choices=genderType.choices, max_length=20)
    weight  = models.FloatField()
    height  = models.FloatField()


class Training(models.Model):
   exerciseId   = models.BigAutoField( primary_key=True)
   exerciseName = models.CharField(max_length=50)
   exerciseType = models.CharField(max_length=100)
   description  = models.TextField()
  # img  =  models.ImageField(upload_to='exercise')


class Advices(models.Model):
    id    = models.BigAutoField( primary_key=True)
    title = models.CharField(max_length=100)
    content=models.TextField()
  #  img   = models.ImageField(upload_to='advice')



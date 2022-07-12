from django.db import models

# Create your models here.
class Authentication(models.Model):
    Username = models.CharField(max_length=100,primary_key=True)
    Password = models.CharField(max_length=100)

from django.db import models

# Create your models here.
class Entries(models.Model):
    fav_subject = models.CharField(max_length=100)
    love_to_do = models.CharField(max_length=100)
    fav_colour = models.CharField(max_length=100)
    fav_game = models.CharField(max_length=100)
    User = models.CharField(max_length=100)
    
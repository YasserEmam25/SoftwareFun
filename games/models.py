from django.db import models

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    desc = models.TextField()

from django.db import models


class Prodcut(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default='default.jpg')
    likes = models.PositiveIntegerField(default=0)
    

class User(models.Model):
    pass
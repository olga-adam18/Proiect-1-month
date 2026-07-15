from django.db import models

# Create your models here.
class Recipe(models.Model):
    name=models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    ingredients=models.TextField()
    time=models.CharField(max_length=50)


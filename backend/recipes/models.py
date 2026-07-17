from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    name=models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    ingredients=models.JSONField()
    time=models.CharField(max_length=50)
    is_default=models.BooleanField(default=False)
    



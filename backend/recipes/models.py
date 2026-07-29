from django.db import models


# Create your models here.

#model for Recipes
class Recipe(models.Model):
    name=models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    ingredients=models.JSONField()
    time=models.CharField(max_length=50)
    is_default=models.BooleanField(default=False)

#model for Products
class Product(models.Model):
    name=models.CharField(max_length=70)
    category=models.CharField(max_length=50)
    calories=models.CharField(max_length=20)
    protein = models.CharField(max_length=20)
    fat = models.CharField(max_length=20)
    carbohydrates=models.CharField(max_length=20)
    description=models.TextField()

    def __str__(self):
        return self.name

#model for Nutrition
class Nutrition(models.Model):
    name=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    description=models.TextField()
    daily_intake=models.TextField()
    sources=models.JSONField()

    def __str__(self):
        return self.name



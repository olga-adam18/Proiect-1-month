from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=70)
    category=models.CharField(max_length=50)
    calories=models.CharField(max_length=20)
    protein = models.CharField(max_length=20)
    fat = models.CharField(max_length=20)
    carbohydrates=models.CharField(max_length=20)
    description=models.TextField()

    class Meta:
        db_table='recipes_product'

    
    def __str__(self):
        return self.name
from django.db import models

# Create your models here.

class Nutrition(models.Model):
    name=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    description=models.TextField()
    daily_intake=models.TextField()
    sources=models.JSONField()

    class Meta:
        db_table="recipes_nutrition"

        
    def __str__(self):
        return self.name



import os
import json
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from recipes.models import Recipe

file_path = os.path.join("data", "recipes.json")

with open(file_path, "r", encoding="utf-8") as file:
    recipes = json.load(file)

print(f"Loaded {len(recipes)} recipes.")

if Recipe.objects.exists():
    print("Rețetele deja există în baza de date")
else:
    for recipe in recipes:
        Recipe.objects.create(
            name=recipe["name"],
            category=recipe["category"],
            ingredients=recipe["ingredients"],
            time=recipe["time"]
        )
    
    print("Rețetele au fost importate cu succes")
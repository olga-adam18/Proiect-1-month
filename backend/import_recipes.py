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
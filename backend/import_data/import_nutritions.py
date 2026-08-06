import json
from nutrition.models import Nutrition


def import_nutrition():

    with open("data/nutrition.json", "r", encoding="utf-8") as file:
        nutritions = json.load(file)


    for nutrition in nutritions:

        Nutrition.objects.create(
            name=nutrition["name"],
            category=nutrition["category"],
            description=nutrition["description"],
            daily_intake=nutrition["daily_intake"],
            sources=nutrition["sources"]
        )

    print("Nutrition imported successfully!")
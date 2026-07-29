import json
from recipes.models import Product


def import_products():

    with open("data/products.json", "r", encoding="utf-8") as file:
        products = json.load(file)


    for product in products:

        Product.objects.create(
            name=product["name"],
            category=product["category"],
            calories=product["calories"],
            protein=product["protein"],
            fat=product["fat"],
            carbohydrates=product["carbohydrates"],
            description=product["description"]
        )

    print("Products imported successfully!")
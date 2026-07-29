from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt # i'm using this for testing with  Postman

#Recipes
from .models import Recipe

#Product
from .models import Product

#Nutrition
from .models import Nutrition


#Recipes API
def get_recipes(request):

    recipes = Recipe.objects.all()  #gather all the rows from the Recipe SQlite

    data=[]

    for recipe in recipes:
        data.append(
            {
                "id":recipe.id,
                "name":recipe.name,
                "category":recipe.category,
                "ingredients":recipe.ingredients,
                "time":recipe.time
            }
        )

    return JsonResponse(data,safe=False)

@csrf_exempt
def get_one_recipe(request,id):
    if request.method != "GET":
        return JsonResponse(
            {"error":"Doar metoda GET este permisă"}, status = 405
        )
    
    try:
        recipe = Recipe.objects.get(id=id)
    except Recipe.DoesNotExist:
        return JsonResponse(
            {"error":"Rețeta nu există"}, status = 404
        )
    
    return JsonResponse(
        {
            "id":recipe.id,
            "name":recipe.name,
            "category":recipe.category,
            "ingredients":recipe.ingredients,
            "time":recipe.time
        } ,  status=200
    )


@csrf_exempt
def add_recipes(request):

    if request.method != "POST":
        return JsonResponse({"EROR":"doar methoda post este permisă"}, status=405)
    
    data = json.loads(request.body)

    recipe = Recipe.objects.create(
        name=data["name"],
        category=data["category"],
        ingredients=data["ingredients"],
        time=data["time"],
        is_default=False
    )
    return JsonResponse(
        {
            "id": recipe.id,
            "message":"Rețetă adăugată cu succes"
        }, status = 201
    )


@csrf_exempt #tells Django not to check the CSRF security token for this view.
def change_recipes_entirely(request,id):
    if request.method != "PUT":
        return JsonResponse(
            {"error":"Doar metoda PUT este permisă"}, status=405
        )
    
    try:
        recipe = Recipe.objects.get(id=id) 

    except Recipe.DoesNotExist:
        return JsonResponse(
            {"error":"Rețeta nu există"},status = 404
        )
    
    if recipe.is_default:
        return JsonResponse(
            {"error": "Nu poți modifica o rețetă implicită"}, status = 403
        )
    
    data = json.loads(request.body)

    recipe.name=data["name"]
    recipe.category=data["category"]
    recipe.ingredients=data["ingredients"]
    recipe.time=data["time"]

    recipe.save()

    return JsonResponse(
        {"message":"Rețeta a fost actualizată"}, status = 200
    )

@csrf_exempt
def update_recipes(request,id):

    if request.method != "PATCH":
        return JsonResponse(
            {"error":"Doar metoda PATCH este permisă"}, status = 405
        ) 
    
    try:
        recipe = Recipe.objects.get(id=id)

    except Recipe.DoesNotExist:
        return JsonResponse(
            {"error":"Rețeta nu există"},status= 404
        )
    
    if recipe.is_default:
        return JsonResponse(
            {"error":"Nu poți modifica o rețetă implicită"},status = 403
        )
    
    data = json.loads(request.body)

    if "name" in data:
        recipe.name=data["name"]
    if "category" in data:
        recipe.category=data["category"]
    if "ingredients" in data:
        recipe.ingredients=data["ingredients"]
    if "time" in data:
        recipe.time=data["time"]

    recipe.save()

    return JsonResponse(
        {"message":"Rețeta a fost modificată parțial"}, status=200
    )

@csrf_exempt
def delete_recipes(request,id):

    if request.method != "DELETE":
        return JsonResponse(
            {"error":"Doar metoda DELETE este permisă"}, status = 405
        )
    
    try:

        recipe = Recipe.objects.get(id=id)
    except Recipe.DoesNotExist:
        return JsonResponse(
            {"error":"Rețeta nu există"}, status = 404
        )
    
    if recipe.is_default:
        return JsonResponse(
            {"error":"Nu poți șterge o rețetă implicită"}, status = 403
        )
    
    recipe.delete()
    return JsonResponse(
        {"message":"Rețeta a fost ștearsă cu succes"}, status=200
    )

#Products API
@csrf_exempt
def get_products(request):
     if request.method == "GET":

        products = Product.objects.all()

        data = []

        for product in products:

            data.append(
                {
                "id": product.id,
                "name": product.name,
                "category": product.category,
                "calories": product.calories,
                "protein": product.protein,
                "fat": product.fat,
                "carbohydrates": product.carbohydrates,
                "description": product.description
                }
            )

        return JsonResponse(data, safe=False)

@csrf_exempt
def get_one_product(request,id):
    if request.method == "GET":

        try:
            product = Product.objects.get(id=id)

            data = {
                "id": product.id,
                "name": product.name,
                "category": product.category,
                "calories": product.calories,
                "protein": product.protein,
                "fat": product.fat,
                "carbohydrates": product.carbohydrates,
                "description": product.description
            }

            return JsonResponse(data)
        except Product.DoesNotExist:

            return JsonResponse({"error": "Product not found"},status=404)

#Nutrition API
@csrf_exempt
def get_nutritions(request):
    if request.method == "GET":

        nutritions = Nutrition.objects.all()

        data = []

        for nutrition in nutritions:
            data.append(
                {
                "id": nutrition.id,
                "name": nutrition.name,
                "category": nutrition.category,
                "description": nutrition.description,
                "daily_intake": nutrition.daily_intake,
                "sources": nutrition.sources
                }
            )

        return JsonResponse(data, safe=False)

@csrf_exempt
def get_one_nutrition(request,id):
    if request.method == "GET":

        try:
            nutrition = Nutrition.objects.get(id=id)

            data = {
                "id": nutrition.id,
                "name": nutrition.name,
                "category": nutrition.category,
                "description": nutrition.description,
                "daily_intake": nutrition.daily_intake,
                "sources": nutrition.sources
            }

            return JsonResponse(data)
        except Nutrition.DoesNotExist:

            return JsonResponse({"error": "Nutrition not found"},status=404)








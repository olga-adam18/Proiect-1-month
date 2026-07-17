from django.http import JsonResponse
from .models import Recipe
import json
from django.views.decorators.csrf import csrf_exempt # i'm using this for testing with tools like Postman

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
def update_recipes(request,id):
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








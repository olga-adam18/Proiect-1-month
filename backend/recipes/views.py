from django.http import JsonResponse
from .models import Recipe
import json
from django.views.decorators.csrf import csrf_exempt

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
        time=data["time"]
    )
    return JsonResponse(
        {
            "id": recipe.id,
            "message":"Rețetă adăugată cu succes"
        }, status = 201
    )






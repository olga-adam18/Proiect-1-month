from django.http import JsonResponse
from .models import Recipe

def get_list(request):

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




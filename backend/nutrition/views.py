from django.shortcuts import render
from django.http import JsonResponse
from .models import Nutrition
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.

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









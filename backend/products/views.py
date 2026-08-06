from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 


# Create your views here.

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

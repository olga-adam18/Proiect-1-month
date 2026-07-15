from django.http import JsonResponse

def get_recipes(request):
    return JsonResponse({"message":"the API worked !"})


# Create your views here.

from django.urls import path
from .views import get_recipes,add_recipes,update_recipes

urlpatterns = [
    path("recipes/", get_recipes),
    path("recipes/add/",add_recipes),
    path("recipes/update/<int:id>/", update_recipes),
]
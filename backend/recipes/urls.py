from django.urls import path
from .views import (
    get_recipes,
    add_recipes,
    update_recipes,delete_recipes,
    change_recipes_entirely,
    get_one_recipe )

urlpatterns = [
    path("recipes/", get_recipes),
    path("recipes/add/",add_recipes),
    path("recipes/patch/<int:id>/", update_recipes),
    path("recipes/put/<int:id>/", change_recipes_entirely),
    path("recipes/delete/<int:id>/",delete_recipes),
    path("recipes/<int:id>/",get_one_recipe)
]
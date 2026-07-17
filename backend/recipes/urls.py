from django.urls import path
from .views import (
    get_recipes,
    add_recipes,
    update_recipes,
    patch_recipes,
    delete_recipes,
    get_one_recipe )

urlpatterns = [
    path("recipes/", get_recipes),
    path("recipes/add/",add_recipes),
    path("recipes/update/<int:id>/", update_recipes),
    path("recipes/patch/<int:id>/", patch_recipes),
    path("recipes/delete/<int:id>/",delete_recipes),
    path("recipes/<int:id>/",get_one_recipe)
]
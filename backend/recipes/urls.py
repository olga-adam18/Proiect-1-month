from django.urls import path
from .views import (
    get_recipes,
    add_recipes,
    update_recipes,delete_recipes,
    change_recipes_entirely,
    get_one_recipe ,
    get_products,
    get_one_product,
    get_nutritions,
    get_one_nutrition)

urlpatterns = [
    #recipes 
    path("recipes/", get_recipes),
    path("recipes/add/",add_recipes),
    path("recipes/patch/<int:id>/", update_recipes),
    path("recipes/put/<int:id>/", change_recipes_entirely),
    path("recipes/delete/<int:id>/",delete_recipes),
    path("recipes/<int:id>/",get_one_recipe),

    #products
    path("products/",get_products),
    path("products/<int:id>/",get_one_product),

    #nutritions
    path("nutritions/",get_nutritions),
    path("nutritions/<int:id>/",get_one_nutrition)
]
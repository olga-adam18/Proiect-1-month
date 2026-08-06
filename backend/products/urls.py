from .views import (get_products,get_one_product)
from django.urls import path

urlpatterns= [
     path("",get_products),
     path("<int:id>/",get_one_product)
]
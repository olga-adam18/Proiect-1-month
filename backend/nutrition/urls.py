from django.urls import path
from .views import (get_nutritions,get_one_nutrition)

urlpatterns = [
    path("",get_nutritions),
    path("<int:id>/",get_one_nutrition)
]
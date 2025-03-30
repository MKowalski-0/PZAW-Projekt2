from django.urls import path
from .views import home, recipe_list

urlpatterns = [
    path('', home, name='home'),
    path('przepisowo/', recipe_list, name='recipe_list'),
]

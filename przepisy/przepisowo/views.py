from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'przepisowo/recipe_list.html', {'przepisowo': recipes})

def home(request):
    return render(request, 'przepisowo/home.html')


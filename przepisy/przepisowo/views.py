from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Recipe, Comment
from .forms import CommentForm

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    comments = recipe.comments.all()

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.user = request.user
            comment.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = CommentForm()

    return render(request, 'przepisowo/recipe_detail.html', {'recipe': recipe, 'comments': comments, 'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Konto zostało stworzone! Możesz teraz się zalogować.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'przepisowo/register.html', {'form': form})


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'przepisowo/recipe_list.html', {'recipes': recipes})

def home(request):
    return render(request, 'przepisowo/home.html')


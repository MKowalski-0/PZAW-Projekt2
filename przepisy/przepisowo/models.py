from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Comment(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.recipe.name}'


class Recipe(models.Model):
    name = models.CharField(max_length=200)  # Nazwa przepisu
    category = models.CharField(max_length=100)  # Kategoria (keto/paleo)
    image = models.ImageField(upload_to='recipe_images/')  # Zdjęcie przepisu
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Cena
    preparation_time = models.PositiveIntegerField()  # Czas w minutach

    def __str__(self):
        return self.name

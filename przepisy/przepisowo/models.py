from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)  # Nazwa przepisu
    category = models.CharField(max_length=100)  # Kategoria (keto/paleo)
    image = models.ImageField(upload_to='recipe_images/')  # Zdjęcie przepisu
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Cena
    preparation_time = models.PositiveIntegerField()  # Czas w minutach

    def __str__(self):
        return self.name

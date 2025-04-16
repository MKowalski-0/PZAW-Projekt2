from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipe_images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    preparation_time = models.PositiveIntegerField()
    preparation_method = models.CharField(max_length=2000, default="")

    def save(self, *args, **kwargs):
        #Skalowanie obrazu przed zapisaniem
        super().save(*args, **kwargs)

        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)
            img = img.resize((300, 300)) 
            img.save(img_path)

    def __str__(self):
        return self.name


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.recipe.name}'

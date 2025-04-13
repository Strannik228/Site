from django.db import models
from django.conf import settings
import os


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
def get_image_choices():
    image_dir = os.path.join(settings.BASE_DIR, "static/images/")
    return [(f"static/images/{img}", img) for img in os.listdir(image_dir) if img.endswith((".jpg", ".png"))]

class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255, choices=get_image_choices())
    def __str__(self):
        return self.name

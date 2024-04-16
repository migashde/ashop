from django.db import models

class Category(models.Model):
    image = models.ImageField(upload_to="static/category_images", default=None)
    name = models.CharField(max_length=200)
    description = models.TextField(default=None)

    def __str__(self):
        return f"{self.name}"

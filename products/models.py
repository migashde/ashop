from django.db import models
from categories.models import Category

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    created_at = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

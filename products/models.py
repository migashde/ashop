from django.db import models
from categories.models import Category

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

class Product_images(models.Model):
    image = models.ImageField(upload_to="static/product_images/%Y/%m/%d/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    updated_at = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now_add=True)
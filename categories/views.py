from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.template import loader

from categories.models import Category
from products.models import Product


def products(request, category_id):
    template = loader.get_template("cat_view.html")
    context = {
        "category": Category.objects.filter(pk=category_id).first(),
        "products": Product.objects.prefetch_related('product_images_set').filter(category_id = category_id),
    }
    return HttpResponse(template.render(context, request))

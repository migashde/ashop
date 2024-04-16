from django.http import HttpResponse
from django.template import loader

from categories.models import Category
from products.models import Product


def home(request):
    template = loader.get_template("home.html")
    context = {
        "categories": Category.objects.all(),
        "products": Product.objects.prefetch_related('product_images_set').all(),
    }
    return HttpResponse(template.render(context, request))

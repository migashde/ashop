from django.http import HttpResponse
from django.template import loader

from products.models import Product

def detail(request, product_id):
    template = loader.get_template("view.html")
    context = {
        "product": Product.objects.filter(pk=product_id),
    }
    return HttpResponse(template.render(context, request))


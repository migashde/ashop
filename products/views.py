from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from categories.models import Category
from products.models import Product, Product_images
from django.contrib.auth.decorators import login_required

def detail(request, product_id):
    template = loader.get_template("view.html")
    context = {
        "product": Product.objects.filter(pk=product_id).first(),
        "product_images": Product_images.objects.filter(product_id=product_id).first(),
    }
    return HttpResponse(template.render(context, request))
  
@login_required(login_url='/login')
def add_view(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        sale = float(request.POST.get("price")) - float(request.POST.get("sale"))
        description = request.POST.get("description")
        category_id = request.POST.get("category")
        images = request.FILES.getlist("images")

        try:
            category = Category.objects.get(id=category_id)
            product = Product(
                product_name=product_name,
                quantity=quantity,
                price=price,
                sale=sale,
                description=description,
                category=category
            )
            product.save()

            for image in images:
                product_image = Product_images(
                    image=image,
                    product=product
                )
                product_image.save()

            return redirect("/")
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")

    else:
        template = loader.get_template("add_product.html")
        context = {
            "category": Category.objects.all(),
        }
        return HttpResponse(template.render(context, request))


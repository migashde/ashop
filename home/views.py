from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
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

def search(request):
    template = loader.get_template("search.html")
    search_value = request.GET.get('search', '').lower()
        
    context = {
        "search_value": search_value,
        "products": Product.objects.prefetch_related('product_images_set').filter(product_name__icontains = search_value),
    }
    return HttpResponse(template.render(context, request))

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    try:
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          return redirect("/")
      else:
          template = loader.get_template("login.html")
          return HttpResponse(template.render())
    except:
      template = loader.get_template("login.html")
      return HttpResponse(template.render())

def logout_view(request):
    logout(request)
    return redirect("/")
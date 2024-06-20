from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.template import loader
from django.db.models import F, Q

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
    template = loader.get_template("product_list.html")
    search_value = request.GET.get('search', '').lower()
        
    context = {
        "title": "Хайсан утга: " + search_value,
        "products": Product.objects.prefetch_related('product_images_set').filter(Q(product_name__icontains=search_value) | Q(description__icontains=search_value)),
    }
    return HttpResponse(template.render(context, request))

def sales(request):
    template = loader.get_template("product_list.html")
        
    context = {
        "title": "Хямдралтай бүтээгдэхүүнүүд",
        "products": Product.objects.prefetch_related('product_images_set').filter(~Q(price=F('sale'))),
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
          print(request.GET["next"])
          
          if (request.GET["next"]):
              return redirect(request.GET["next"])
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

def contact(request):
    template = loader.get_template("contact.html")
 
    return HttpResponse(template.render())
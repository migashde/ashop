"""
URL configuration for ashop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views as home
from products import views as product
from categories import views as category
from cart import views as cart
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home.home, name="home"),
    path('category/<int:category_id>', category.products, name="cat_products"),
    path('product/<int:product_id>', product.detail, name="detail"),
    path('product/add', product.add_view, name="add"),
    path('login', home.login_view, name="login"),
    path('logout', home.logout_view, name="logout"),
    path('cart/add/<int:product_id>', cart.add_to_cart, name="cart_add"),
    path('cart/view', cart.cart_view, name="cart_view"),
    path('cart/checkout', cart.checkout, name="checkout"),
    path('search', home.search, name="search"),
    path('sales', home.sales, name="sales"),
    path('contact', home.contact, name="contact"),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

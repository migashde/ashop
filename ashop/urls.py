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
from cart.cart import Cart
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home.home, name="home"),
    path('product/<int:product_id>', product.detail, name="detail"),
    path('product/add', product.add_view, name="add"),
    path('login', home.login_view, name="login"),
    path('logout', home.logout_view, name="logout"),
    path('cart/add/<int:product_id>', Cart.add, name="cart_add"),
    path('cart/remove', Cart.remove, name="cart_remove"),
    path('cart/total', Cart.get_sub_total_price, name="cart_total"),
    path('cart/clear', Cart.clear, name="cart_clear"),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

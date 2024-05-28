from django.utils.deprecation import MiddlewareMixin
from .cart import Cart

class CartMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not hasattr(request, 'cart'):
            request.cart = Cart(request)
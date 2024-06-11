from django.shortcuts import redirect, render

from products.models import Product

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {'quantity': 1, 'product_id': product_id}

    request.session['cart'] = cart
    return redirect('cart_view')
  
def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []

    for product_id, item in cart.items():
        product = Product.objects.get(pk=product_id)
        cart_items.append({
            'product': product,
            'quantity': item['quantity']
        })

    return render(request, 'cart_view.html', {'cart_items': cart_items})
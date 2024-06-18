from django.shortcuts import redirect, render

from products.models import Product

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {'quantity': 1, 'product_id': product_id}

    request.session['cart'] = cart
    return redirect('/cart/view')
  
def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, item in cart.items():
        product = Product.objects.get(pk=product_id)
        cart_items.append({
            'product': product,
            'quantity': item['quantity']
        })
        total_price += product.sale
        
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }

    return render(request, 'cart_view.html', context)

def checkout(request):
    cart = request.session.get('cart', {})
    total_price = 0
    
    for product_id in cart:
        product = Product.objects.get(pk=product_id)
        total_price += product.sale
        
    return render(request, 'checkout.html', {'total_price': total_price })
def cart_items(request):
    cart = request.session.get('cart', {})
    return {'cart_items': cart}
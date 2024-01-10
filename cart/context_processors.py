from .models import Cart, CartItem
from .views import _cart_id


def total_count(request):
    total_count = 0
    if "admin" in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                total_count += cart_item.product.price * cart_item.quantity
        except Cart.DoesNotExist:
            total_count = 0

    return dict(total_count=total_count)

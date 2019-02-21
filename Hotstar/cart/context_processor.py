from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
    # This means if admin word is in url then return nothing
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            # The QuerySet value for an exact lookup must be limited to one result using slicing.
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)

# This context_processor.py should be registered in settings.py - TEMPLATES - context_processors option
# This function is wriiten only to count the number of quantity in cart_items
# This dict value passed is used in navbar.html
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .cart import Cart
from Shop.models import Product

def cart_add(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cart = request.session.get('cart', {})

        already_in_cart = product_id in cart
        cart[product_id] = cart.get(product_id, 0) + 1

        request.session['cart'] = cart

        return JsonResponse({
            'qty': sum(cart.values()),
            'exists': already_in_cart
        })
    
def cart_view(request):
        cart = request.session.get("cart", [])
        products = []
        for item in cart:
            try:
                product = Product.objects.get(pk=item['product_id'])
                quantity = item.get("quantity", 1)
                for _ in range(quantity):
                    products.append(product)
            except Product.DoesNotExist:
                continue
        return render(request, "cart/cart_summary.html", {"products": products})

def cart_delete(request):
    cart = request.session.get('cart', {})
    if request.method == 'POST' and request.POST.get('action') == 'post':
        product_id = str(request.POST.get('product_id'))
        if product_id in cart:
            if cart[product_id] > 1:
                cart[product_id] -= 1  # فقط کم می‌کنیم
            else:
                del cart[product_id]  # اگه فقط یکی مونده بود، حذف می‌کنیم
            request.session['cart'] = cart
            request.session.modified = True
            return JsonResponse({
                'success': True,
                'qty': sum(cart.values())
            })
        return JsonResponse({'success': False, 'message': 'Product not in cart'})
    return JsonResponse({'success': False, 'message': 'Invalid request'})

def cart_summary(request):
    cart = Cart(request)
    products = []

    for item_id in cart.cart.keys():
        try:
            product = Product.objects.get(pk=int(item_id))
            quantity = cart.cart[item_id].get('quantity', 1) if isinstance(cart.cart[item_id], dict) else cart.cart[item_id]
            for _ in range(quantity):
                products.append(product)
        except (ValueError, TypeError, Product.DoesNotExist):
            continue

    return render(request, 'cart/cart_summary.html', {'products': products})
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if cart is None:
            cart = {}
            self.session['cart'] = cart
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart or not isinstance(self.cart[product_id], dict):
            price = str(product.price)
            qty = self.cart.get(product_id, 0)
            self.cart[product_id] = {
                'price': price,
                'quantity': qty + 1
            }
        else:
            self.cart[product_id]['quantity'] += 1
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True

    def __len__(self):
        total = 0
        for item in self.cart.values():
            if isinstance(item, dict):
                total += int(item.get('quantity', 0))
            elif isinstance(item, int):
                total += item
        return total
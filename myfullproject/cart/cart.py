
class Cart():
    def __init__(self,request):
        self.session = request.session

        # get the current session key

        cart = self.session.get('S_key')

        # if user is new, create key

        if 'S_key' not in request.session:
            cart = self.session['S_key'] = {}

            # make cart available in all pages

            self.cart = cart
    
    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass


        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True
from cart import Cart

def carrito(request):
	print "hola"
	return dict(cart=Cart(request))
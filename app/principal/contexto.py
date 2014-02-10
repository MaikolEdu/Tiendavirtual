from cart import Cart
from django.http import HttpResponse
from app.principal.models import Categoria,CategoriaSubCategoria

def carrito(request):
	print "hola"
	return dict(cart=Cart(request))

def subcategoria(request):
	categorias = Categoria.objects.all()
	subcategorias = CategoriaSubCategoria.objects.all()
	datos = []
	for i in categorias:
		subcat = subcategorias.filter(categoria__id = i.id)
		sub = []
		for x in subcat:
			sub.append({
				'nombre' : x.subcategoria.nombre,
				'id' : x.id
				})
		datos.append({
			'categoria' : i.nombre,
			'id': i.id,
			'sub' : sub
			})
		
	return dict(datos = datos)

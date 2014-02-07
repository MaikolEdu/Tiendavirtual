from app.principal.models import Producto,CategoriaSubCategoria,Categoria
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
import json

from cart import Cart

# Carrito de compras

def ajax_carrito(request):
	producto_id=request.POST["producto_id"]
	cantidad = request.POST["cantidad"]	
	product = producto.objects.get(id=producto_id)
	cart = Cart(request)
	cart.add(product, product.precio, cantidad)
	return HttpResponse(1)

def ajax_eliminaritem(request):
	product_id=request.POST["item_id"]
 	product = producto.objects.get(id=product_id)
 	cart = Cart(request)
 	cart.remove(product)
 	total_carrito =cart.total_cart
 	print total_carrito
 	return HttpResponse(total_carrito)


def get_cart(request):
    return render_to_response('cart.html', dict(cart=Cart(request)), context_instance=RequestContext(request))

#####

def inicio(request):
	productos = Producto.objects.order_by('-id')[:4]
	catsubcat = Categoria.objects.order_by('id')[:3]
	return render_to_response('index.html',{'productos':productos}, context_instance=RequestContext(request))


def utiles_escolares(request):
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
			'sub' : sub
			})
	productos =  Producto.objects.filter(categoriasubcategoria__id = subcategorias[0].id).values('nombre','stock','img','precio') 
	return render_to_response('utiles_escolares.html',{'datos':datos,'productos':productos}, context_instance=RequestContext(request))	


def ajax_ver_subcategorias(request):
	if request.is_ajax():
		if request.method=="POST":
			productos = Producto.objects.filter(categoriasubcategoria__id = request.POST['id'])
			data = serializers.serialize('json', productos,fields = ( 'pk','nombre','stock','precio','img'))
			return HttpResponse(data , mimetype="application/json")


"""
# def ajax_ver_productos(request):
# 	if request.is_ajax():
# 		if request.method=="POST":
# 			pk=request.POST['id']
# 			subcategorias = CategoriaSubCategoria.objects.filter(categoria__id = pk)
# 			data = serializers.serialize('json', subcategorias)
# 			print data
# 			return HttpResponse(data , mimetype="application/json")
"""


from app.principal.models import Producto,CategoriaSubCategoria,Categoria
from app.principal.forms import SuscripcionForm
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
	product = Producto.objects.get(id=producto_id)
	cart = Cart(request)
	cart.add(product, product.precio, cantidad)
	ultimo_item=dict(cart=Cart(request))
	for item in ultimo_item:
		print str(item.product.nombre)
	return HttpResponse(ultimo_item)

def ajax_eliminaritem(request):
	product_id=request.POST["item_id"]
 	product = Producto.objects.get(id=product_id)
 	cart = Cart(request)
 	cart.remove(product)
 	total_carrito =cart.total_cart
 	print total_carrito
 	return HttpResponse(total_carrito)

#####

def inicio(request):
	productos = Producto.objects.order_by('-id')[:4]
	productoss = Producto.objects.order_by('?')[:10]
	data = []
	datos = []
	for x in productoss:
		data.append({
			'nombre':x.nombre,
			'img':x.img,
			'precio':x.precio,
			'id':x.id
			})
	datos.append(data[:4])
	datos.append(data[4:8])
	datos.append(data[8:10])
	return render_to_response('index.html',{'productos':productos, 'otros':datos}, context_instance=RequestContext(request))

def utiles_escolares(request):
	productos =  Producto.objects.filter(categoriasubcategoria__categoria__id = 1).values('nombre','stock','img','precio') 
	return render_to_response('Productos.html',{'productos':productos}, context_instance=RequestContext(request))

def utiles_oficina(request):
	productos =  Producto.objects.filter(categoriasubcategoria__categoria__id = 2).values('nombre','stock','img','precio') 
	return render_to_response('Productos.html',{'productos':productos}, context_instance=RequestContext(request))

def regalos(request):
	productos =  Producto.objects.filter(categoriasubcategoria__categoria__id = 3).values('nombre','stock','img','precio') 
	return render_to_response('Productos.html',{'productos':productos}, context_instance=RequestContext(request))

def ajax_ver_subcategorias(request):
	if request.is_ajax():
		if request.method=="POST":
			productos = Producto.objects.filter(categoriasubcategoria__id = request.POST['id'])
			data = serializers.serialize('json', productos,fields = ( 'pk','nombre','stock','precio','img'))
			return HttpResponse(data , mimetype="application/json")

def ver_detalle(request,id_producto):
	producto = Producto.objects.get(id=id_producto)
	caracteristicas =  producto.Caracteristicavalor.all()
	return render_to_response('Descripcion.html', {'producto':producto, 'caracteristicas':caracteristicas}, context_instance=RequestContext(request))


def ajax_registar_suscripcion(request):
	if request.is_ajax():
		if request.method == 'POST':
			correo = SuscripcionForm(request.POST)
			if correo.is_valid():
				correo.save()
				dato = True
	else:
		dato = False
	return HttpResponse(dato)

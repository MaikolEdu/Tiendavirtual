from app.principal.models import Producto,CategoriaSubCategoria,Categoria
from app.principal.forms import SuscripcionForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
import json
from cart import Cart
from django.core.mail import EmailMessage
from mailchimp import utils
# Carrito de compras

def ajax_carrito(request):

	if request.is_ajax():
		producto_id=request.POST["producto_id"]
		cantidad = request.POST["cantidad"]	
        try :
            product = Producto.objects.get(id=producto_id)
            cart = Cart(request)
            cart.add(product, product.precio, cantidad)
            print product.precio
            data ={'nombre':product.nombre,'precio':str(product.precio)}
            print data
            return HttpResponse(data)
        except :
        	return HttpResponse("/")
	else:
		raise Http404

def ajax_eliminaritem(request):
	product_id=request.POST["item_id"]
 	product = Producto.objects.get(id=product_id)
 	cart = Cart(request)
 	cart.remove(product)
 	total_carrito =cart.total_cart
 	return HttpResponse(total_carrito)

def inicio(request):
	productos = Producto.objects.order_by('-id')[:4]
	productoss = Producto.objects.order_by('?')[:12]
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
	datos.append(data[8:12])
	return render_to_response('index.html',{'productos':productos, 'otros':datos}, context_instance=RequestContext(request))

def utiles_escolares(request):
	productos =  Producto.objects.filter(categoriasubcategoria__categoria__id = 1).values('nombre','stock','img','precio','id') 
	return render_to_response('Productos.html',{'productos':productos}, context_instance=RequestContext(request))

def utiles_oficina(request):
	productos =  Producto.objects.filter(categoriasubcategoria__categoria__id = 2).values('nombre','stock','img','precio','id') 
	return render_to_response('Productos.html',{'productos':productos}, context_instance=RequestContext(request))

def regalos(request):
	productos =  Producto.objects.filter(categoriasubcategoria__categoria__id = 3).values('nombre','stock','img','precio','id') 
	return render_to_response('Productos.html',{'productos':productos}, context_instance=RequestContext(request))

def ajax_ver_subcategorias(request):
	if request.is_ajax():
		if request.method=="POST":
			productos = Producto.objects.filter(categoriasubcategoria__id = request.POST['id'])
			data = serializers.serialize('json', productos,fields = ( 'pk','nombre','stock','precio','img','id'))
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
				msg = EmailMessage(subject="Bienvenido al e-comerce", from_email="LA empresa <micky_1390@outlook.com>",
					to=[request.POST['email']])
				msg.template_name = "Nuevo"
				msg.template_content = {                  
					"contenido" :  "<h1>HOLAAAAAAAAAAAA Bienvenido a este e-comerce</h1>"
				}
				msg.send()
				lista = utils.get_connection().get_list_by_id('5a8860d1e1')
				lista.subscribe(request.POST['email'], {'EMAIL': request.POST['email'], 'FNAME': request.POST['nombre']})
				dato = 1
			else:
				dato = 2
	else:
		dato = 0
	return HttpResponse(dato)

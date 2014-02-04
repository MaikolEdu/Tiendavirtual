from app.principal.models import Producto,CategoriaSubCategoria,Categoria
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
import json


def inicio(request):
	productos = Producto.objects.order_by('-id')[:4]
	productoss = Producto.objects.order_by('?')[:10]
	d =[]
	for x in xrange(len( productoss)):
	 	print "inicio %s" % x
	 	for j in xrange(x,x+3):
	 		print j
	 	x = j + 1
	 	print "fin %s" % x
	 	
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
	return render_to_response('Productos.html',{'datos':datos,'productos':productos}, context_instance=RequestContext(request))	


def ajax_ver_subcategorias(request):
	if request.is_ajax():
		if request.method=="POST":
			productos = Producto.objects.filter(categoriasubcategoria__id = request.POST['id'])
			data = serializers.serialize('json', productos,fields = ( 'pk','nombre','stock','precio','img'))
			return HttpResponse(data , mimetype="application/json")


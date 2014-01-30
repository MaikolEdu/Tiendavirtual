from app.principal.models import Producto,CategoriaSubCategoria,Categoria
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
import json


def inicio(request):
	productos = Producto.objects.order_by('-id')[:4]
	catsubcat = Categoria.objects.order_by('id')[:3]
	return render_to_response('index.html',{'productos':productos}, context_instance=RequestContext(request))

def utiles_escolares(request):
	categorias = Categoria.objects.values('id','nombre')
	subcategorias = CategoriaSubCategoria.objects.filter(categoria__id = categorias[0]['id']).values('subcategoria__nombre','id')
	productos =  Producto.objects.filter(categoriasubcategoria__id = subcategorias[0]['id']).values('nombre','stock','img')
	return render_to_response('utiles_escolares.html',{'cat':categorias,'sub': subcategorias, 'pro':productos }, context_instance=RequestContext(request))	

def ajax_ver_subcategorias(request):
	if request.is_ajax():
		if request.method=="POST":
			pk=request.POST['id']
			subcategorias = CategoriaSubCategoria.objects.filter(categoria__id = pk)
			ct = []
			for i in subcategorias:
				ct.append(
					{
					'nombre' : i.subcategoria.nombre,
					'pk' : i.id
					})
			print ct
			data = json.dumps(ct)
			return HttpResponse(data , mimetype="application/json")


# def ajax_ver_productos(request):
# 	if request.is_ajax():
# 		if request.method=="POST":
# 			pk=request.POST['id']
# 			subcategorias = CategoriaSubCategoria.objects.filter(categoria__id = pk)
# 			data = serializers.serialize('json', subcategorias)
# 			print data
# 			return HttpResponse(data , mimetype="application/json")

from app.principal.models import Producto
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def inicio(request):
	productos= Producto.objects.all()
	return render_to_response('index.html',{'productos':productos}, context_instance=RequestContext(request))

def utiles_escolares(request):
	datos = []
	


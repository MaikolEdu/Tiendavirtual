from app.principal.models import Producto
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def productos(request):
	print request.session.session_key
	productos= Producto.objects.all()
	return render_to_response('lista_productos.html',{'productos':productos}, context_instance=RequestContext(request))

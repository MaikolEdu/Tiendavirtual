from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^TiendaVirtual/', include('TiendaVirtual.foo.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # url de las paginas
    url(r'^$','app.principal.views.inicio'),

    url(r'^utiles_escolares/$','app.principal.views.utiles_escolares'),
    url(r'^utiles_oficina/$','app.principal.views.utiles_oficina'),
    url(r'^regalos/$','app.principal.views.regalos'),
    url(r'^ajax/ver_subcategoria/$', 'app.principal.views.ajax_ver_subcategorias'),
    url(r'^productos/(?P<id_producto>\d+)$', 'app.principal.views.ver_detalle'),

    #carrito
    url(r'^ajax_carrito/$', 'app.principal.views.ajax_carrito'),
    url(r'^ajax_eliminaritem/$', 'app.principal.views.ajax_eliminaritem'),
    #url(r'^vercarrito/$', 'app.principal.views.get_cart'),

    url(r'^ajax/suscribirse/$','app.principal.views.ajax_registar_suscripcion'),




)



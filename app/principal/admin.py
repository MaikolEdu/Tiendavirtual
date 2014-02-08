from app.principal.models import *
from django.contrib import admin
from django import forms



class AdminEntries(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['nombre'] }

class ProductoAdmin(admin.ModelAdmin):
	filter_horizontal = ('categoriasubcategoria',)
	prepopulated_fields = { 'slug': ['nombre'] }


admin.site.register(Categoria, AdminEntries)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(SubCategoria, AdminEntries)
admin.site.register(CategoriaSubCategoria)
admin.site.register(Valor)
admin.site.register(Caracteristica)
admin.site.register(Ofertas)
admin.site.register(Suscripciones)


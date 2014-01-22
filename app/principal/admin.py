from app.principal.models import *
from django.contrib import admin
from django import forms



class AdminEntries(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['nombre'] }


admin.site.register(Producto, AdminEntries)

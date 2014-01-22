from principal.models import *
from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class AdminEntries(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['nombre'] }


admin.site.register(Producto, AdminEntries)

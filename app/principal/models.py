#encoding:utf-8
from django.db import models
from django.template import defaultfilters

"""
Modelo : Categoria
con sus respectivo atributo
ejemplos : utiles escolares, 
"""
class Categoria(models.Model):
    nombre = models.CharField(max_length = 30 )

    def __unicode__(self):
        return unicode(self.nombre)    


"""
Modelo : Caracteristica
con sus respectivos atributos
ejemplos : tamaño, color
"""
class Caracteristica(models.Model):
    nombre = models.CharField(max_length = 20)

    def __unicode__(self):
        return unicode(self.nombre)    


"""
Modelo : Valor
con sus respectivos atributos
ejemplos : a4, verde
"""
class Valor(models.Model):
    nombre = models.CharField(max_length = 20)
    caracteristica =  models.ForeignKey(Caracteristica)
    def __unicode__(self):
        return unicode(self.caracteristica.nombre + ':' + self.nombre)

"""
Modelo : Sub-Categoria 
con sus respectivos atributos
eleccion de una categoria por defecto tenemos 3
ejemplos :  cuadernos , lapiceros, folders 
"""
class SubCategoria(models.Model):

    nombre =  models.CharField(max_length = 200)
    slug =  models.SlugField(max_length = 200)
    categoria = models.ManyToManyField(Categoria)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.nombre)
        super(SubCategoria, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.categoria.nombre + ' : ' + self.nombre)

"""
Modelo : Producto
con sus respectivos atributos
ejemplos : cuaderno Loro 
"""
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=10, decimal_places=3)
    slug = models.SlugField(max_length=200)
    stock = models.IntegerField()   
    img=models.FileField(upload_to='imgProducto/')
    subcategoria = models.ManyToManyField(SubCategoria)
    Caracteristicavalor = models.ManyToManyField(Valor)
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.nombre)
        super(Producto, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.nombre)

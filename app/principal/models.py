from django.db import models
from django.template import defaultfilters


class Categoria(models.Model):
        nombre = models.CharField(max_length=200)
        
        def save(self, *args, **kwargs):
                self.slug = defaultfilters.slugify(self.nombre)
                super(Producto, self).save(*args, **kwargs)

        def __unicode__(self):
                return unicode(self.nombre)

class Producto(models.Model):
        nombre = models.CharField(max_length=200)
        descripcion= models.CharField(null=True,blank=True,max_length=100)
        marca = models.CharField(max_length=50)                
        modelo = models.CharField(max_length=50)
        precio=models.DecimalField(max_digits=10, decimal_places=3)
        slug = models.SlugField(max_length=200)        
        adicional_condicion=models.CharField(null=True,blank=True,max_length=100)        
        img=models.FileField(upload_to='imgProducto/')        
        def save(self, *args, **kwargs):
                self.slug = defaultfilters.slugify(self.nombre)
                super(Producto, self).save(*args, **kwargs)

        def __unicode__(self):
                return unicode(self.nombre)


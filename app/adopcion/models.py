from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Persona(models.Model):
   nombre=models.CharField(max_length=50)
   apellido=models.CharField(max_length=70)
   edad=models.IntegerField()
   telefono=models.CharField(max_length=10)
   email=models.EmailField()
   domicilio=models.TextField()
   def __unicode__(self):
      return '{} {}'.format(self.nombre,self.apellido)

class Solicitud(models.Model):
   persona=models.ForeignKey(Persona,null=True,blank=True)
   numero_mascotas=models.IntegerField()
   razones=models.TextField()

class Producto(models.Model):
   TIPO_PRODUCTO =(
      (1, "Simple"),
      (2, "Variable"),
      (3, "Servicio"),
   )
   uuid = models.CharField(max_length=50)
   codigo = models.CharField(max_length=50)
   nombre = models.CharField(max_length=50)
   descripcion = models.TextField(max_length=50)
   marca = models.CharField(max_length=50)
   modelo = models.CharField(max_length=50)
   tipo_producto = models.IntegerField(choices=TIPO_PRODUCTO)
   comentario = models.TextField(max_length=100)
   precio_compra = models.FloatField(max_length=50)
   precio_venta = models.FloatField(max_length=50)
   precio_variaciones = models.FloatField(max_length=50)
   procenta_comision = models.FloatField(max_length=50)
   porcenta_monedero = models.FloatField(max_length=50)
   porcenta_descuento = models.FloatField(max_length=50)
   activo = models.BooleanField()
   existencia = models.IntegerField()

   def __unicode__(self):
      return self.nombre

class Atributo(models.Model):
   uuid = models.CharField(max_length=50)
   nombre = models.CharField(max_length=50)
   unico = models.BooleanField()

   def __unicode__(self):
      return self.nombre


class AtributoValor(models.Model):
   atributo_id = models.ForeignKey(Atributo, on_delete=models.CASCADE)
   uuid = models.CharField(max_length=50)
   nombre = models.CharField(max_length=50)
   def __unicode__(self):
      return self.nombre
class Variaciones(models.Model):
   producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
   activo = models.BooleanField()
   existencia = models.IntegerField()
   atributos = models.ManyToManyField(AtributoValor)


# class ProductosAtributos(models.Model):
#    producto_id = models.ManyToManyField(Variaciones)
#    atributo_valor_id = model.ManyToManyField(AtributoValor)

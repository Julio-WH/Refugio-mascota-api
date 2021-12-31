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

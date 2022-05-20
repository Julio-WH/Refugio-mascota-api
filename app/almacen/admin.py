# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.almacen.models import Producto, Atributo, AtributoValor, Variaciones, CategoriaProducto


class ListVariaciones(admin.TabularInline):
    model = Variaciones
    extra = 0


class ListVariacionesValue(admin.TabularInline):
    model = AtributoValor
    extra = 0


@admin.register(Producto)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'descripcion', 'precio_compra', 'precio_venta', 'existencia', 'tipo_producto')
    inlines = [ListVariaciones]


@admin.register(Atributo)
class VariacionesAdmin(admin.ModelAdmin):
    inlines = [ListVariacionesValue]


admin.site.register(CategoriaProducto)

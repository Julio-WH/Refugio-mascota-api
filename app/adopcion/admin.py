from django.contrib import admin
from app.adopcion.models import Persona, Producto, Atributo, AtributoValor, Variaciones

class ListVariaciones(admin.TabularInline):
    model = Variaciones

@admin.register(Producto)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'descripcion', 'precio_compra', 'precio_venta', 'existencia', 'tipo_producto')
    inlines = [ListVariaciones]

# class VariacionesAdmin(admin.ModelAdmin):
#     list_display = ('producto_id', 'atributos')
# Register your models here.
admin.site.register(Persona)
# admin.site.register(Producto, ProductosAdmin)
admin.site.register(Atributo)
admin.site.register(AtributoValor)
admin.site.register(Variaciones)

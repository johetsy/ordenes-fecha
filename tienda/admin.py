from django.contrib import admin

from tienda.models import Orden, Producto, Detalle
# Register your models here.
class DetalleInline(admin.StackedInline):
    model = Detalle
    extra =0


class OrdenAdmin(admin.ModelAdmin):
    list_display = ("cliente", "direccion")
    inlines = [DetalleInline]

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion")


class DetalleAdmin(admin.ModelAdmin):
    list_display = ("orden_link", "producto_link", "cantidad", "precio", "sub_total")

    # --------------------------------------------
    # modificacion para que el administrador aparezca el 
    # precio del producto al crear un detalle
    exclude = ["precio"]

    def save_model(self, request, obj, form, change):
        obj.precio = obj.producto.precio 
        super().save_model(request, obj, form, change)
    # --------------------------------------------------------
    def orden_link(self, obj):
        return obj.orden.cliente
    orden_link.short_description = "Orden"

    def producto_link(self, obj):
        return obj.producto.nombre
    producto_link.short_description = "Product"    
    

    def sub_total(self, obj):
        return obj.precio * obj.cantidad
    

admin.site.register(Orden, OrdenAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Detalle, DetalleAdmin)
    
from django.contrib import admin
from .models import *
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','telefono',]
    list_display_links = ['rut','nombre','telefono',]
    search_fields = ['rut','nombre','telefono',]

class ProductoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Descripcion', {
          'fields': ('nombre','categoria','proveedor')  
        }),
        ('Variables', {
            'fields': ('precio','stock')
        }),
    )

class ProductoInline(admin.StackedInline):
    model = Producto
    extra = 0
    fields = ['nombre','precio','stock','categoria','proveedor']

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','web','direccion','telefono']
    list_display_links = ['rut','nombre','web','direccion','telefono']
    search_fields = ['nombre','rut']
    inlines = [ProductoInline]

class VentaAdmin(admin.ModelAdmin):
    list_display = ['cliente','fecha','monto_final','isDescuento']
    list_display_links = ['cliente','fecha','monto_final']

    actions = ['aplicarDescuento','quitarDescuento']

    def aplicarDescuento(self,request,queryset):
        queryset.update(descuento=True)
    aplicarDescuento.short_description = "Aplicar Descuento"

    def quitarDescuento(self,request,queryset):
        queryset.update(descuento=False)    
    quitarDescuento.short_description = "Quitar Descuento"

admin.site.register(Categoria)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Venta,VentaAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Detalle)
from django.contrib import admin

from .models import Proveedor, Contacto

# Se reemplazaron los admin.site.register con los decoradores @admin.register
# admin.site.register(Proveedor)
# admin.site.register(Contacto)


@admin.register(Proveedor)
class AdminProduct(admin.ModelAdmin):
    list_display = ('nombre', 'identificacion', 'telefono', 'notas',)


@admin.register(Contacto)
class AdminContacto(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'empresa', 'celular',
                    'email', 'cargo',)
    list_filter = ('empresa',)

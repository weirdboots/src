from django.contrib import admin

from .models import Remision, ItemRemisionado

# Se reemplazaron los admin.site.register con los decoradores @admin.register
# admin.site.register(Remision)
# admin.site.register(ItemRemisionado)


@admin.register(Remision)
class AdminRemision(admin.ModelAdmin):
    list_display = ('empresa', 'codigoremision', 'fechainicio',
                    'fechavenc', 'valorbruto', )
    list_filter = ('empresa', 'fechainicio', 'fechavenc', )


@admin.register(ItemRemisionado)
class AdminItemRemisionado(admin.ModelAdmin):
    list_display = ('remision', 'refprovee', 'refinterna',
                    'cantidad', 'valorunidad', )
    list_filter = ('remision', 'refprovee', 'refinterna', )

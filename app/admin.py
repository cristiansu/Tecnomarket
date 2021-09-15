from django.contrib import admin
from .models import Marca, Producto, Contacto

# Register your models here. Para esto se importan los modelos desde views.py. luego se ingresan las líneas de 
#admin.site.register(nombreModelo)

class ProductoAdmin(admin.ModelAdmin):
    list_display=['nombre','precio','nuevo','marca']
    list_editable=['precio']
    search_fields=['nombre']
    list_filter=['marca','nuevo']
    list_per_page=5



admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)

from .models import CategoríaProd, Producto
from django.contrib import admin

# Register your models here.

class CategoríaProdAdmin(admin.ModelAdmin):
    readonly_fields=("creado", "actualizado")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("creado", "actualizado")


admin.site.register(CategoríaProd, CategoríaProdAdmin)
admin.site.register(Producto, ProductoAdmin)


from django.contrib import admin
from .models import *

# Register your models here.

class CategoriaPostAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

admin.site.register(Categoria, CategoriaPostAdmin)
admin.site.register(Post, CategoriaPostAdmin)
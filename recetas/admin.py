from django.contrib import admin
from .models import Receta

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'tiempo_preparacion', 'autor', 'fecha_creacion')
    list_filter = ('categoria', 'fecha_creacion')
    search_fields = ('titulo', 'ingredientes')
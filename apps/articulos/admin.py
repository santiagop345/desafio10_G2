from django.contrib import admin
from .models import Categoria, Etiqueta, Articulo

# Register your models here.

@admin.register(Articulo)
class ArticulosAdmin(admin.ModelAdmin):

    list_display = ('id', 'titulo' ,'bajada', 'fecha_actualiz', 
                    'publicado', 'contenido', 'activo', 'categoria',
                    'imagen', 'fecha_creacion', 'etiqueta')
                    
admin.site.register(Categoria)
admin.site.register(Etiqueta)    
    
    
     
    
   
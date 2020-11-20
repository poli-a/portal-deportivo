from django.contrib import admin
from .models import Noticia
from .models import Categoria

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'usuario', 'fecha_publicacion', 'status')
    list_filter = ('status', 'created', 'fecha_publicacion', 'usuario')
    search_fields = ('titulo', 'nota')
    prepopulated_fields = {'slug': ('titulo',)}
    raw_id_fields = ('usuario',)
    date_hierarchy = 'fecha_publicacion'
    ordering = ('status', 'fecha_publicacion')
admin.site.register(Categoria)
from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'nombre', 'apellido', 'imagen']
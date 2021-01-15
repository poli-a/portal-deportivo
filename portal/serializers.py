from rest_framework import serializers
from .models import *

class NoticiaSerializers(serializers.ModelSerializer):
    username = serializers.CharField(read_only = True, source = "usuario.username")
    nombreCategoria = serializers.CharField(read_only = True, source = "categoria.nombre")
    class Meta:
        model = Noticia
        exclude = ['created', 'updated']

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
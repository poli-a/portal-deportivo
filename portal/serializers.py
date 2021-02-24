from rest_framework import serializers
from .models import *

class NoticiaSerializers(serializers.ModelSerializer):
    username = serializers.CharField(read_only = True, source = "usuario.username")
    nombreCategoria = serializers.CharField(read_only = True, source = "categoria.nombre")
    media_url = serializers.CharField(read_only = True, source = "img.url")
    
    class Meta:
        model = Noticia
        exclude = ['created', 'updated']    

class CategoriaSerializers(serializers.ModelSerializer):
    # Metodo para validar nombre de categoria #
    def validate_nombre(self, value):
        e = Categoria.objects.filter(nombre__iexact = value).exists()
        if e:
            raise serializers.ValidationError('Esta categoria ya existe')
        return value

    class Meta:
        model = Categoria
        fields = '__all__'    
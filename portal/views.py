from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import *

class NoticiaViewset(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializers

    # Metodo para obtener noticias por categoria #
    def get_queryset(self):
        noticias = Noticia.objects.all()
        categoria = self.request.GET.get('categoria')

        if categoria:
            noticias = Noticia.objects.filter(categoria = categoria)
        
        return noticias
    

class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers
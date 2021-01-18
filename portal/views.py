from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import *
from rest_framework.pagination import PageNumberPagination


# Clase para paginacion de resultados de json #
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100

class NoticiaViewset(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializers
    pagination_class = StandardResultsSetPagination

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
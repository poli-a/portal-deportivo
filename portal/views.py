from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import *

class NoticiaViewset(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializers
import json
# Rest Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Models
from competiciones.models import Tabla, Partido
# Serializers
from competiciones.serializers import TablaSerializer

@api_view(['GET', 'POST'])
def tabla_posiciones_api_view(request):

    # Lista Tablas de Posiciones #
    if request.method == 'GET': 
        tablas = Tabla.objects.all()
        # attr many p/ serializar la lista de tablas de posiciones #
        tabla_serializer = TablaSerializer(tablas, many = True)
        return Response(tabla_serializer.data)

    # Crea nueva tabla de posiciones #
    elif request.method == 'POST':

        tabla_serializer = TablaSerializer(data = request.data, many = True)
        if tabla_serializer.is_valid():
            tabla_serializer.save()
            return Response(tabla_serializer.data, status = status.HTTP_201_CREATED)
        return Response(tabla_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def tabla_posiciones_detail_api_view(request, pk=None):

    # Queryset p/ obtener datos de una tabla de posiciones #
    tabla = Tabla.objects.filter(id = pk).first()
    
    if tabla:
    
        # Devuelve el detalle de una tabla de posiciones #
        if request.method == 'GET':
            tabla_serializer = TablaSerializer(tabla)
            return Response(tabla_serializer.data)

        # Actualiza datos de una tabla de posiciones #
        elif request.method == 'PUT':

            # En el parametro data se le pasa la info a actualizar #
            tabla_serializer = TablaSerializer(tabla, data = request.data)
            if tabla_serializer.is_valid():
                tabla_serializer.save()
                return Response(tabla_serializer.data)
            return Response(tabla_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # Elimina una Tabla de posiciones por su id #
        elif request.method == 'DELETE':

            partidos = Partido.objects.filter(fixture_id = tabla.fixture_id)
            if partidos:
                return Response({'message': 'No se puede eliminar esta tabla de posiciones porque el fixture asociado posee partidos cargados. Elimine todos lo partidos cargados y asociados al fixture antes de eliminar la tabla de posiciones.'})

            tabla.delete()
            return Response({'message': 'Tabla de posiciones eliminada.'})

    return Response({'message': 'No se encontro tabla de posiciones con ese id.'}, status = status.HTTP_400_BAD_REQUEST)
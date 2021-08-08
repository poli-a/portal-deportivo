import json
# Rest Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Models
from competiciones.models import Fixture, Tabla, Partido
# Serializers
from competiciones.serializers import FixtureSerializer

@api_view(['GET', 'POST'])
def fixture_api_view(request):

    # Lista fixtures #
    if request.method == 'GET': 
        fixtures = Fixture.objects.all()
        # attr many p/ serializar la lista de fixtures
        fixture_serializer = FixtureSerializer(fixtures, many = True)
        return Response(fixture_serializer.data)

    # Crea nuevo fixture #
    elif request.method == 'POST':
        
        request = calcularCantPartidos(request)
        
        fixture_serializer = FixtureSerializer(data = request.data)
        if fixture_serializer.is_valid():
            fixture_serializer.save()
            return Response(fixture_serializer.data, status = status.HTTP_201_CREATED)
        return Response(fixture_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def fixture_detail_api_view(request, pk=None):

    # Queryset p/ obtener datos de un fixtures #
    fixture = Fixture.objects.filter(id = pk).first()
    
    if fixture:
    
        # Devuelve el detalle de un fixtures #
        if request.method == 'GET':
            # devuelve un fixture o un string vacio #
            fixture_serializer = FixtureSerializer(fixture)
            return Response(fixture_serializer.data)

        # Actualiza datos de un Fixture #
        elif request.method == 'PUT':

            request = calcularCantPartidos(request)

            # En el parametro data se le pasa la info a actualizar #
            fixture_serializer = FixtureSerializer(fixture, data = request.data)
            if fixture_serializer.is_valid():
                fixture_serializer.save()
                return Response(fixture_serializer.data)
            return Response(fixture_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # Elimina un Fixture por su id #
        elif request.method == 'DELETE':
            
            tabla = Tabla.objects.filter(fixture_id = fixture.id).first()
            if tabla:
                return Response({'message': 'No se puede eliminar el fixture porque posee tabla de posiciones asociada'})

            partido = Partido.objects.filter(fixture_id = fixture.id).first()
            if partido:
                return Response({'message': 'No se puede eliminar el fixture porque posee partidos asociados'})

            fixture.delete()
            return Response({'message': 'Fixture eliminado.'})

    return Response({'message': 'No se encontro competicion con ese id.'}, status = status.HTTP_400_BAD_REQUEST)

# Calcula la cantidad de partidos para el fixture segun la cant de equipos y la modalidad #
def calcularCantPartidos(request):

    # Modalidad partido unico #
    if request.data['modalidad'] == 'partido_unico':
        request.data['cantidad_partidos'] = 1
    # Modalidad torneo los equipos se enfrentan todos contra todos #
    if request.data['modalidad'] == 'torneo':
        request.data['cantidad_partidos'] = request.data['cantidad_equipos'] * (request.data['cantidad_equipos'] - 1)
        
    # Modalidad playoff, empareja a los equipos p/ eliminacion directa #
    if request.data['modalidad'] == 'playoff':
        request.data['cantidad_partidos'] = request.data['cantidad_equipos'] / 2

    # Duplica la cant de partidos si corresponde jugar ida y vuelta #
    if request.data['ida_vuelta'] == True:
        request.data['cantidad_partidos'] = request.data['cantidad_partidos'] * 2

    return request
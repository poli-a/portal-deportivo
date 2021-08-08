# Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Models
from competiciones.models import Competicion, Fixture, Ranking_Gol, Ranking_Tarjeta
# Serializers
from competiciones.serializers import CompeticionSerializer

@api_view(['GET', 'POST'])
def competicion_api_view(request):

    # Lista competiciones #
    if request.method == 'GET': 
        competiciones = Competicion.objects.all()
        # attr many p/ serializar la lista de competiciones
        competiciones_serializer = CompeticionSerializer(competiciones, many = True)
        return Response(competiciones_serializer.data)

    # Crea nueva competicion #
    elif request.method == 'POST':
        competicion_serializer = CompeticionSerializer(data = request.data)
        if competicion_serializer.is_valid():
            competicion_serializer.save()
            return Response(competicion_serializer.data, status = status.HTTP_201_CREATED)
        return Response(competicion_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def competicion_detail_api_view(request, pk=None):

    # Queryset p/ obtener datos de una competicion #
    competicion = Competicion.objects.filter(id = pk).first()
    
    if competicion:
    
        # Devuelve el detalle de una competicion #
        if request.method == 'GET':
            # devuelve una competicion o un string vacio #
            competicion_serializer = CompeticionSerializer(competicion)
            return Response(competicion_serializer.data)

        # Actualiza datos de una competicion #
        elif request.method == 'PUT':
            # En el parametro data se le pasa la info a actualizar #
            competicion_serializer = CompeticionSerializer(competicion, data = request.data)
            if competicion_serializer.is_valid():
                competicion_serializer.save()
                return Response(competicion_serializer.data)
            return Response(competicion_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # Elimina una competicion por su id #
        elif request.method == 'DELETE':
            
            # Validando que no existan fixtures asociados a la competicion #
            fixture = Fixture.objects.filter(competicion_id = competicion.id).first()
            if fixture:
                return Response({'message': 'No se puede eliminar la competicion porque posee fixtures asociados'})

            # Validando que no exista ranking de goleadores asociados a la competicion #
            ranking_gol = Ranking_Gol.objects.filter(competicion_id = competicion.id).first()
            if ranking_gol:
                return Response({'message': 'No se puede eliminar la competicion porque posee ranking de goleadores asociado.'})
            
            # Validando que no exista ranking de tarjetas asociados a la competicion #
            ranking_tarj = Ranking_Tarjeta.objects.filter(competicion_id = competicion.id).first()
            if ranking_tarj:
                return Response({'message': 'No se puede eliminar la competicion porque posee ranking de tarjetas asociado.'})
                
            competicion.delete()
            return Response({'message': 'Competicion eliminada.'})

    return Response({'message': 'No se encontro competicion con ese id.'}, status = status.HTTP_400_BAD_REQUEST)
# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from users.serializers import UserLoginSerializer, UserModelSerializer

# Models
from django.contrib.auth.models import User

class UserViewSet(viewsets.GenericViewSet):

    # Validando si el user esta activo
    queryset = User.objects.filter(is_active=True)
    # Serializer de referencia
    serializer_class = UserModelSerializer

    # Detail define si es una petición de detalle o no, método permitido: post
    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in. Envio de datos al serializer y validando"""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
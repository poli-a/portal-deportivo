# Django
from django.contrib.auth import password_validation, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Django REST Framework
from rest_framework import serializers

# Models
"""from django.contrib.auth.models import User"""
from users.models import User

class UserModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        )

class UserLoginSerializer(serializers.Serializer):

    # Campos requeridos
    username = serializers.CharField()
    password = serializers.CharField(min_length=6, max_length=64)

    # validando datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardando usuario
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

class UserSignUpSerializer(serializers.ModelSerializer):

    # Campos requeridos
    username = serializers.CharField()
    password = serializers.CharField(min_length=6, max_length=64)

    # Metodo para validar username unico #
    def validate_username(self, value):
        e = User.objects.filter(username__iexact = value).exists()
        if e:
            raise serializers.ValidationError('Este username ya existe')
        return value
    
    class Meta:
        model = User
        fields = '__all__'   
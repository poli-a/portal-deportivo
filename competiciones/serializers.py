from rest_framework import serializers
from competiciones.models import *

class CompeticionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competicion
        exclude = ['usuario']

class FixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixture
        fields  = '__all__'

class TablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabla
        fields  = '__all__'
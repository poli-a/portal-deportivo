from rest_framework import serializers
from competiciones.models import Competicion, Fixture

class CompeticionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competicion
        exclude = ['usuario']

class FixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixture
        fields  = '__all__'
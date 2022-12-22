from rest_framework import serializers

from mnt.models import Produccion, Cultivo, Cliente


class ProduccionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Produccion
        fields='__all__'


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model=Cliente
        fields='__all__'

class CultivoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Cultivo
        fields='__all__'

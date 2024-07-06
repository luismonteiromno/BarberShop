from rest_framework import serializers

from ..models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    credito = serializers.ReadOnlyField()
    
    class Meta:
        model = Cliente
        fields = '__all__'
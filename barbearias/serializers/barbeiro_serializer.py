from rest_framework import serializers

from ..models import Barbeiro


class BarbeiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barbeiro
        fields = '__all__'
        
    def validate_salario(self, value):
        if value < 0:
            raise serializers.ValidationError('O salário não pode ser negativo.')
        return value
        
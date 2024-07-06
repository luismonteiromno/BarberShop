from rest_framework import serializers

from ..models import Aviso


class AvisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aviso
        fields = '__all__'

    def validate_data_de_inicio(self, value):
        data_de_inicio = self.initial_data.get('data_de_inicio')
        data_de_encerramento = self.initial_data.get('data_de_encerramento')
        if data_de_inicio >= data_de_encerramento:
            raise serializers.ValidationError('A data de início do aviso não pode ser maior/igual à data de encerramento.')
        return value
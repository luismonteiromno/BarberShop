from rest_framework import serializers
from ..models import Funcionario


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

    def validate_salario(self, value):
        if value < 0:
            raise serializers.ValidationError(
                'O salário não pode ser negativo!'
            )
        return value

    def validate_cargo(self, value):
        if value is None:
            raise serializers.ValidationError('O cargo é obrigatório!')
        return value

    def validate_barbearia(self, value):
        if value is None:
            raise serializers.ValidationError('A barbearia do funcionário é obrigatório!')
        return value
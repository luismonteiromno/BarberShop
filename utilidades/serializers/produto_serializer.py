from rest_framework import serializers
from ..models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

    def validate_preco(self, value):
        if value <= 0:
            raise serializers.ValidationError('O preço não pode ser negativo.')
        return value
    
    def validate_quantidade(self, value):
        if value <= 0:
            raise serializers.ValidationError('A quantidade não pode ser negativa.')
        return value
    
    def validate_barbearia(self, value):
        if value is None:
            raise serializers.ValidationError('A barbearia é obrigatória!')
        return value
        
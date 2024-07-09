from rest_framework import serializers

from ..models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'
        # read_only_fields = ['avaliacao', 'barbearia', 'comentario', 'usuario']
        
    def validate_avaliacao(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError('A avaliação precisa ser um número entre 0 e 5.')
        return value
    
    def validate_barbearia(self, value):
        if value is None:
            raise serializers.ValidationError('A barbearia é obrigatória!')
        return value
        
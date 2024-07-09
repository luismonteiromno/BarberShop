from rest_framework import serializers

from ..models import Promocao


class PromocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocao
        fields = '__all__'
        
    def validate_inicio_da_promocao(self, value):
        inicio = self.initial_data.get('inicio_da_promocao')
        fim = self.initial_data.get('fim_da_promocao')
        if inicio >= fim:
            raise serializers.ValidationError('A data de início da promoção não pode ser maior ou igual à data de encerramento.')
        return value
    
    def validate_servico(self, value):
        servico = self.initial_data.get('servico')
        plano_de_fidelidade = self.initial_data.get('plano_de_fidelidade')
        if servico is None or plano_de_fidelidade is None:
            raise serializers.ValidationError('A promoção deve ser para um serviço ou plano de fidelidade!')
        return value
        
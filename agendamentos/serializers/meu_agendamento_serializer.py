from rest_framework import serializers

from ..models import MeuAgendamento


class MeuAgendamentoSerializer(serializers.ModelSerializer):
    servico = serializers.SerializerMethodField()
    
    def get_servico(self, obj):
        return str(obj.servico)
    
    class Meta:
        model = MeuAgendamento
        fields = '__all__'
        read_only_fields = [
            'agendamento'
        ]
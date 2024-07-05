from rest_framework import serializers

from ..models import Agendamento
import pendulum

class AgendamentoSerializer(serializers.ModelSerializer):
    agendamento_cancelado = serializers.ReadOnlyField()
    numero_do_agendamento = serializers.ReadOnlyField()
    
    def validate_data_marcada(self, value): 
        if value < pendulum.now():
            raise serializers.ValidationError('A data do agendamento não pode ser anterior à data de hoje.')
        return value
    
    class Meta:
        model = Agendamento
        fields = '__all__'
        
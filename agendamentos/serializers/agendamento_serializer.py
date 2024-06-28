from rest_framework import serializers

from ..models import Agendamento


class AgendamentoSerializer(serializers.ModelSerializer):
    numero_do_agendamento = serializers.ReadOnlyField()
    
    class Meta:
        model = Agendamento
        fields = '__all__'
        
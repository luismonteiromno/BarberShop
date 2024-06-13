from rest_framework.serializers import ModelSerializer
from ..models import MeuAgendamento

class MeuAgendamentoSerializer(ModelSerializer):
    class Meta:
        model = MeuAgendamento
        fields = '__all__'
        read_only_fields = [
            'agendamento'
        ]
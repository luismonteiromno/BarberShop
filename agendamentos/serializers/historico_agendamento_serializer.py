from rest_framework.serializers import ModelSerializer
from ..models import HistoricoDeAgendamento

class HistoricoDeAgendamentoSerializer(ModelSerializer):
    class Meta:
        model = HistoricoDeAgendamento
        fields = '__all__'
        
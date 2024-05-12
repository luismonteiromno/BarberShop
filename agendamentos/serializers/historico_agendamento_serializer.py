from rest_framework.serializers import ModelSerializer
from ..models import HistoricoDeAgendamento

class HistoricoDeAgendamentoSerializer(ModelSerializer):
    class Meta:
        model = HistoricoDeAgendamento
        fields = '__all__'
        read_only_fields = [
            'preco_do_servico',
            'data_do_agendamento',
            'servico_fornecido',
            'cliente',
            'barbeiro'
        ]
        
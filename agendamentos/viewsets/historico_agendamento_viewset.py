from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import HistoricoDeAgendamento
from ..serializers import HistoricoDeAgendamentoSerializer

class HistoricoDeAgendamentoViewSet(ModelViewSet):
    queryset = HistoricoDeAgendamento.objects.all()
    serializer_class = HistoricoDeAgendamentoSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'servico_fornecido',
        'cliente',
        'barbeiro',
    ]
    
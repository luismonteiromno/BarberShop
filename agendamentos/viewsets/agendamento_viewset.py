from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Agendamento
from ..serializers import AgendamentoSerializer

class AgendamentoViewSet(ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'servico'
    ]

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

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
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        servico = self.request.query_params.get('servico')
        
        queryset = queryset.filter(
                Q(cliente=self.request.user) |
                Q(barbeiro=self.request.user)
            )
        
        if servico:
            queryset = queryset.filter(servico_fornecido__nome_do_servico__icontains=servico)
                  
        return queryset
    
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import MeuAgendamento
from ..serializers import MeuAgendamentoSerializer


class MeuAgendamentoViewSet(ModelViewSet):
    queryset = MeuAgendamento.objects.all()
    serializer_class = MeuAgendamentoSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'cliente',
    ]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        if not self.request.user.is_superuser:
            queryset = queryset.filter(cliente=self.request.user)
            
        return queryset
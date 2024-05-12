from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from ..models import Agendamento
from ..serializers import AgendamentoSerializer

class AgendamentoViewSet(ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'servico'
    ]
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        
        queryset = queryset.filter(
            Q(escolher_barbeiro=self.request.user) |
            Q(usuario=self.request.user)
        )
        
        return queryset

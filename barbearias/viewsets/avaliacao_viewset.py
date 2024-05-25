from decimal import Decimal

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import Avaliacao
from ..serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'barbearia'
    ]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        nome_da_barbearia = self.request.query_params.get('nome_da_barbearia')
        avaliacao =  self.request.query_params.get('avaliacao')
        
        if nome_da_barbearia:
            queryset = queryset.filter(barbearia__nome_da_barbearia__icontains=nome_da_barbearia)
            
        if avaliacao:
            queryset = queryset.filter(avaliacao=Decimal(avaliacao))
        
        return queryset
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import MetodoDePagamento
from ..serializers import MetodoDePagamentoSerializer


class MetodoDePagamentoViewSet(ModelViewSet):
    queryset = MetodoDePagamento.objects.all()
    serializer_class = MetodoDePagamentoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        metodo = self.request.query_params.get('metodo')
        
        if metodo:
            queryset = queryset.filter(metodo_de_pagamento=metodo)
            
        return queryset

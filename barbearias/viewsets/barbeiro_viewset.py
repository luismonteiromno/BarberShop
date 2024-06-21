from decimal import Decimal

from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import Barbeiro
from ..serializers import BarbeiroSerializer


class BarbeiroViewSet(ModelViewSet):
    queryset = Barbeiro.objects.all()
    serializer_class = BarbeiroSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'barbeiro'
    ]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        por_barbearia = self.request.query_params.get('por_barbearia')
        nome_do_barbeiro =  self.request.query_params.get('nome_do_barbeiro')
        media_de_avaliacao = self.request.query_params.get('media_de_avaliacao')
        
        if not self.request.user.is_superuser:
            queryset = queryset.filter(
                Q(barbearia__dono=self.request.user) | 
                Q(funcionarios=self.request.user)
            )
        
        if por_barbearia:
            queryset = queryset.filter(barbearia__nome_da_barbearia__icontains=por_barbearia)
            
        if nome_do_barbeiro:
            queryset = queryset.filter(barbeiro__username__icontains=nome_do_barbeiro)
            
        if media_de_avaliacao:
            queryset = queryset.filter(avaliacao=Decimal(media_de_avaliacao))
            
        return queryset
    
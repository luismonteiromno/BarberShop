from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import Barbearia
from ..serializers import BarbeariaSerializer


class BarbeariaViewSet(ModelViewSet):
    queryset = Barbearia.objects.all()
    serializer_class = BarbeariaSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'nome_da_barbearia'
    ]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        if not self.request.user.is_superuser:
            queryset = queryset.filter(
                Q(dono=self.request.user) |
                Q(funcionarios=self.request.user)
            )
            
        tipo_da_barbearia = self.request.query_params.get('tipo_da_barbearia')
        
        if tipo_da_barbearia:
            queryset = queryset.filter(tipo_de_barbearia=tipo_da_barbearia)
        
        return queryset
    
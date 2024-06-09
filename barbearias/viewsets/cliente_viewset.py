from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Cliente
from ..serializers import ClienteSerializer


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'cliente',
        'plano_de_fidelidade',
    ]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        if not self.request.user.is_superuser:
            queryset = queryset.filter(cliente=self.request.user)
            
        barbearia = self.request.query_params.get('barbearia')
        
        if barbearia:
            queryset = queryset.filter(plano_de_fidelidade__barbearia__nome_da_barbearia__icontains=barbearia) 

        return queryset
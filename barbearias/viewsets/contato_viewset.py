from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Contato
from ..serializers import ContatoSerializer

class ContatoViewSet(ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        barbearia = self.request.query_params.get('barbearia')
        
        if barbearia:
            queryset = queryset.filter(barbearia__nome_da_barbearia__icontains=barbearia)
        
        return queryset
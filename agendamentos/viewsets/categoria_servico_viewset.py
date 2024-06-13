from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import CategoriaDoServico
from ..serializers import CategoriaDoServicoSerializer

class CategoriaDoServicoViewSet(ModelViewSet):
    queryset = CategoriaDoServico.objects.all()
    serializer_class = CategoriaDoServicoSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'nome'
    ]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        categoria = self.request.query_params.get('categoria')
        
        if categoria:
            queryset = queryset.filter(nome__icontains=categoria)
            
        return queryset
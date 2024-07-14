from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Cargo
from ..serializers import CargoSerializer


class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'nome_do_cargo',
        'nivel_hierarquico',
    ]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        funcao = self.request.query_params.get('funcao')
        
        if funcao:
            queryset = queryset.filter(nivel_hierarquico__icontains=funcao)
            
        return queryset

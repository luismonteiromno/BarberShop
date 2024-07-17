from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from ..models import ChavePix
from ..serializers import ChavePixSerializer


class ChavePixViewSet(ModelViewSet):
    queryset = ChavePix.objects.all()
    serializer_class = ChavePixSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'pix',
    ]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        cliente = self.request.query_params.get('cliente')
        
        if cliente:
            queryset = queryset.filter(cliente=cliente)
            
        return queryset

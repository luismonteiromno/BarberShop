from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Aviso
from ..serializers import AvisoSerializer

class AvisoViewSet(ModelViewSet):
    queryset = Aviso.objects.all()
    serializer_class = AvisoSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'barbearia'
    ]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        barbearia = self.request.query_params.get('barbearia')
        data_de_inicio = self.request.query_params.get('data_de_inicio')
        data_de_encerramento = self.request.query_params.get('data_de_encerramento')
        
        if barbearia:
            queryset = queryset.filter(barbearia=barbearia)
                     
        if data_de_inicio:
            queryset = queryset.filter(data_de_inicio__gte=data_de_inicio)
            
        if data_de_encerramento:
            queryset = queryset.filter(data_de_encerramento__lt=data_de_encerramento)
        
        return queryset
    
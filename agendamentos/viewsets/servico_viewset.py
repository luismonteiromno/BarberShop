from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Servico
from ..serializers import ServicoSerializer

class ServicoViewSet(ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'nome_do_servico'
    ]
    
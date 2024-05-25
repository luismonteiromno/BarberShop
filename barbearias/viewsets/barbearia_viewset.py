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
    
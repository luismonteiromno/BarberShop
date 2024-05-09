from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Avaliacao
from ..serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'barbearia'
    ]
    
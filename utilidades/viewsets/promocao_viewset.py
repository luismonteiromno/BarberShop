from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Promocao
from ..serializers import PromocaoSerializer

class PromocaoViewSet(ModelViewSet):
    queryset = Promocao.objects.all()
    serializer_class = PromocaoSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'servico'
    ]
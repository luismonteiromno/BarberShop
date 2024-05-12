from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Barbeiro
from ..serializers import BarbeiroSerializer

class BarbeiroViewSet(ModelViewSet):
    queryset = Barbeiro.objects.all()
    serializer_class = BarbeiroSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'nome_do_barbeiro'
    ]
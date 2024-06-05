from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Financeiro
from ..serializers import FinanceiroSerializer


class FinanceiroViewSet(ModelViewSet):
    queryset = Financeiro.objects.all()
    serializer_class = FinanceiroSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'barbearia'
    ]
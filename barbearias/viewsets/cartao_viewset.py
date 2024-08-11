from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import Cartao
from ..serializers import CartaoSerializer


class CartaoViewSet(ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = [
        'numero',
        'validade',
        'cvv',
    ]

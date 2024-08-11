from decimal import Decimal

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import Produto
from ..serializers import ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()

        categoria = self.request.query_params.get('categoria')
        preco_menor_que = self.request.query_params.get('preco_menor_que')
        preco = self.request.query_params.get('preco')
        preco_maior_que = self.request.query_params.get('preco_maior_que')

        if categoria:
            queryset = queryset.filter(categorias__nome=categoria)

        if preco_menor_que:
            queryset = queryset.filter(preco__lte=Decimal(preco_menor_que))

        if preco:
            queryset = queryset.filter(preco=Decimal(preco))

        if preco_maior_que:
            queryset = queryset.filter(preco__gte=Decimal(preco_maior_que))

        return queryset

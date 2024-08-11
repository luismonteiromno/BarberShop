from decimal import Decimal

from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import Financeiro
from ..serializers import FinanceiroSerializer


class FinanceiroViewSet(ModelViewSet):
    queryset = Financeiro.objects.all()
    serializer_class = FinanceiroSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = ['barbearia']

    def get_queryset(self):
        queryset = super().get_queryset()

        barbearia = self.request.query_params.get('nome_da_barbearia')
        lucro_total = self.request.query_params.get('lucro_total')
        lucro_total_menor = self.request.query_params.get('lucro_total_menor')
        lucro_total_maior = self.request.query_params.get('lucro_total_maior')
        lucro_mensal = self.request.query_params.get('lucro_mensal')
        lucro_planos = self.request.query_params.get('lucro_planos')
        lucro_produtos = self.request.query_params.get('lucro_produtos')
        lucro = self.request.query_params.get('lucro')
        receita_total = self.request.query_params.get('receita_total')

        if not self.request.user.is_superuser:
            queryset = queryset.filter(
                Q(barbearia__dono=self.request.user)
                | Q(barbearia__funcionarios=self.request.user)
            )

        if barbearia:
            queryset = queryset.filter(
                barbearia__nome_da_barbearia__icontains=barbearia
            )

        if lucro_total:
            queryset = queryset.filter(lucro_total=Decimal(lucro_total))

        if lucro_total_menor:
            queryset = queryset.filter(
                lucro_total__lt=Decimal(lucro_total_menor)
            )

        if lucro_total_maior:
            queryset = queryset.filter(
                lucro_total__gt=Decimal(lucro_total_maior)
            )

        if lucro_mensal:
            queryset = queryset.filter(renda_mensal=Decimal(lucro_mensal))

        if lucro_planos:
            queryset = queryset.filter(lucro_planos=Decimal(lucro_planos))

        if lucro_produtos:
            queryset = queryset.filter(lucro_produtos=Decimal(lucro_produtos))

        if receita_total:
            queryset = queryset.filter(receita_total=Decimal(receita_total))

        if lucro:
            if lucro in ['false', 'False']:
                queryset = queryset.filter(prejuizo=True)
            elif lucro in ['true', 'True']:
                queryset = queryset.filter(lucro=True)

        return queryset

    def create(self, request, *args, **kwargs):
        from rest_framework import status
        from rest_framework.response import Response

        return Response(
            {'error': 'Essa ação não está disponivel'},
            status=status.HTTP_403_FORBIDDEN,
        )

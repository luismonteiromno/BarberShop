from datetime import datetime

from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import Promocao
from ..serializers import PromocaoSerializer


class PromocaoViewSet(ModelViewSet):
    queryset = Promocao.objects.all()
    serializer_class = PromocaoSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = [
        'servico',
    ]

    def get_queryset(self):
        queryset = super().get_queryset()

        nome_do_servico = self.request.query_params.get('nome_do_servico')
        mes_da_promocao = self.request.query_params.get('mes_da_promocao')
        inicio_da_promocao = self.request.query_params.get(
            'inicio_da_promocao'
        )
        fim_da_promocao = self.request.query_params.get('fim_da_promocao')
        barbearia = self.request.query_params.get('barbearia')
        plano_fidelidade = self.request.query_params.get('plano_fidelidade')

        if not self.request.user.is_superuser:
            queryset = queryset.filter(
                servico__disponivel_na_barbearia__dono=self.request.user
            )

        if mes_da_promocao:
            queryset = queryset.filter(
                inicio_da_promocao__month=mes_da_promocao
            )

        if nome_do_servico:
            queryset = queryset.filter(
                servico__nome_do_servico__icontains=nome_do_servico
            )

        if barbearia:
            queryset = queryset.filter(
                servico__disponivel_na_barbearia__nome_da_barbearia__iexact=barbearia,
            )

        if plano_fidelidade:
            queryset = queryset.filter(
                plano_fidelidade__nome__icontains=plano_fidelidade
            )

        if inicio_da_promocao:
            queryset = queryset.filter(
                inicio_da_promocao__gte=inicio_da_promocao
            )

        if fim_da_promocao:
            queryset = queryset.filter(fim_da_promocao__lte=fim_da_promocao)

        return queryset.order_by('inicio_da_promocao')

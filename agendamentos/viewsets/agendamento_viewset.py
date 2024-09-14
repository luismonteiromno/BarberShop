from datetime import datetime

from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..models import Agendamento
from ..serializers import AgendamentoSerializer


class AgendamentoViewSet(ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = ['servico']

    def get_queryset(self):
        now = datetime.now()
        queryset = super().get_queryset()

        servico = self.request.query_params.get('servico')
        numero_do_agendamento = self.request.query_params.get(
            'numero_do_agendamento'
        )
        cliente = self.request.query_params.get('cliente')
        barbeiro = self.request.query_params.get('barbeiro')

        if not self.request.user.is_superuser:
            queryset = queryset.filter(
                Q(data_marcada__gte=now)
                & Q(
                    Q(escolher_barbeiro=self.request.user)
                    | Q(cliente=self.request.user)
                )
            )

        if barbeiro:
            queryset = queryset.filter(
                Q(escolher_barbeiro__username__icontains=barbeiro)
                | Q(escolher_barbeiro__cliente__email__icontains=barbeiro)
            )

        if cliente:
            queryset = queryset.filter(
                Q(cliente__cliente__username__icontains=cliente)
                | Q(cliente__cliente__email__icontains=cliente)
            )

        if servico:
            queryset = queryset.filter(
                servico__nome_do_servico__icontains=servico
            )

        if numero_do_agendamento:
            queryset = queryset.filter(
                numero_do_agendamento__icontains=numero_do_agendamento
            )

        return queryset

    @action(detail=False, methods=['GET'])
    def ordenar_por_data_proxima(self, request):
        queryset = (
            self.get_queryset()
            .exclude(passou_da_data=True)
            .order_by('data_marcada')
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

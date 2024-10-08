from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import Aviso
from ..serializers import AvisoSerializer


class AvisoViewSet(ModelViewSet):
    queryset = Aviso.objects.all()
    serializer_class = AvisoSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = ['barbearia']

    def get_queryset(self):
        now = datetime.now().date()
        queryset = super().get_queryset()

        nome_da_barbearia = self.request.query_params.get('nome_da_barbearia')
        data_de_inicio = self.request.query_params.get('data_de_inicio')
        data_de_encerramento = self.request.query_params.get(
            'data_de_encerramento'
        )

        queryset = queryset.exclude(data_de_encerramento__lte=now)

        if nome_da_barbearia:
            queryset = queryset.filter(
                barbearia__nome_da_barbearia__icontains=nome_da_barbearia
            )

        if data_de_inicio:
            queryset = queryset.filter(data_de_inicio__gte=data_de_inicio)

        if data_de_encerramento:
            queryset = queryset.filter(
                data_de_encerramento__lte=data_de_encerramento
            )

        return queryset

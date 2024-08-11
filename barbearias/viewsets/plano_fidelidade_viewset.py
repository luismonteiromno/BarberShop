import django.db
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import PlanosDeFidelidade
from ..serializers import PlanosDeFidelidadeSerializer


class PlanosDeFidelidadeViewSet(ModelViewSet):
    queryset = PlanosDeFidelidade.objects.all()
    serializer_class = PlanosDeFidelidadeSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = [
        'barbearia',
    ]

    def get_queryset(self):
        queryset = super().get_queryset()

        barbearia = self.request.query_params.get('nome_da_barbearia')
        nome_do_plano = self.request.query_params.get('plano_fidelidade')
        clientes = self.request.query_params.get('clientes')

        if not self.request.user.is_superuser:
            queryset = queryset.filter(barbearia__dono=self.request.user)

        if barbearia:
            queryset = queryset.filter(
                barbearia__nome_da_barbearia__icontains=barbearia
            )

        if nome_do_plano:
            queryset = queryset.filter(nome__icontains=nome_do_plano)

        if clientes:
            queryset = queryset.filter(usuarios=int(clientes))

        return queryset

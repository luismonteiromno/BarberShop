from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import Funcionario
from ..serializers import FuncionarioSerializer


class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = [
        'nome',
    ]

    def get_queryset(self):
        queryset = super().get_queryset()

        barbearia = self.request.query_params.get('barbearia')
        cargo = self.request.query_params.get('cargo')
        clt = self.request.query_params.get('clt')
        cpf = self.request.query_params.get('cpf')
        nivel = self.request.query_params.get('nivel')
        pj = self.request.query_params.get('pj')
        salario = self.request.query_params.get('salario')
        salario_maior_que = self.request.query_params.get('salario_maior_que')
        salario_menor_que = self.request.query_params.get('salario_menor_que')

        if barbearia:
            queryset = queryset.filter(
                barbearia__nome_da_barbearia__icontains=barbearia
            )

        if cargo:
            queryset = queryset.filter(cargo__nome_do_cargo__icontains=cargo)

        if clt:
            queryset = queryset.filter(clt=clt)

        if cpf:
            queryset = queryset.filter(cpf=cpf)

        if nivel:
            queryset = queryset.filter(
                cargo__nivel_hierarquico__icontains=nivel
            )

        if pj:
            queryset = queryset.filter(pj=pj)

        if salario:
            queryset = queryset.filter(salario=salario)

        if salario_maior_que:
            queryset = queryset.filter(salario__gt=salario_maior_que)

        if salario_menor_que:
            queryset = queryset.filter(salario__lt=salario_menor_que)

        return queryset

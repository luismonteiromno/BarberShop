from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from ..models import Funcionario
from ..serializers import FuncionarioSerializer


class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'nome',
        'cpf',
    ]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        barbearia = self.request.query_params.get('barbearia')
        cargo = self.request.query_params.get('cargo')
        nivel = self.request.query_params.get('nivel')
        salario = self.request.query_params.get('salario')
        salario_maior_que = self.request.query_params.get('salario_maior_que')
        salario_menor_que = self.request.query_params.get('salario_menor_que')
        
        if barbearia:
            queryset = queryset.filter(barbearia__nome_da_barbearia__icontains=barbearia)
            
        if cargo:
            queryset = queryset.filter(cargo__nome_do_cargo__icontains=cargo)
            
        if nivel:
            queryset = queryset.filter(cargo__nivel_hierarquico__icontains=nivel)
            
        if salario:
            queryset = queryset.filter(salario=salario)
            
        if salario_maior_que:
            queryset = queryset.filter(salario__gt=salario_maior_que)
            
        if salario_menor_que:
            queryset = queryset.filter(salario__lt=salario_menor_que)
                        
        return queryset
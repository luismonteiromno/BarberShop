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
        'cargo',
    ]
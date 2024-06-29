from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Cargo
from ..serializers import CargoSerializer


class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'nome_do_cargo',
        'nivel_hierarquico',
    ]
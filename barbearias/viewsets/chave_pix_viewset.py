from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ..models import ChavePix
from ..serializers import ChavePixSerializer


class ChavePixViewSet(ModelViewSet):
    queryset = ChavePix.objects.all()
    serializer_class = ChavePixSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = [
        'pix',
    ]

    def get_queryset(self):
        queryset = super().get_queryset()

        cliente = self.request.query_params.get('cliente')
        chave_aleatoria = self.request.query_params.get('chave_aleatoria')

        if cliente:
            queryset = queryset.filter(
                Q(cliente__cliente__username__icontains=cliente)
                | Q(cliente__cliente__email__icontains=cliente)
            )

        if chave_aleatoria in ['false', 'False']:
            queryset = queryset.filter(chave_aleatoria=False)

        elif chave_aleatoria in ['true', 'True']:
            queryset = queryset.filter(chave_aleatoria=True)

        return queryset

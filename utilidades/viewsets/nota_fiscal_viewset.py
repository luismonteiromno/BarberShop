from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ..models import NotaFiscal
from ..serializers import NotaFiscalSerializer


class NotaFiscalViewSet(ModelViewSet):
    queryset = NotaFiscal.objects.all()
    serializer_class = NotaFiscalSerializer
    permission_classes = [IsAuthenticated]

    filterset_fields = ['cliente']

    def create(self, request, *args, **kwargs):
        return Response(
            {'error': 'Nota fiscal não pode ser criada com este método.'},
            status=status.HTTP_403_FORBIDDEN,
        )

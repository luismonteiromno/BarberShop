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
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        valor_total = self.request.query_params.get('valor_total')
        status = self.request.query_params.get('status')
        
        if valor_total:
            queryset = queryset.filter(valor_total__gte=valor_total)
            
        if status:
            queryset = queryset.filter(status=status)
        
        return queryset

    def create(self, request, *args, **kwargs):
        return Response(
            {'error': 'Nota fiscal não pode ser criada com este método.'},
            status=status.HTTP_403_FORBIDDEN,
        )

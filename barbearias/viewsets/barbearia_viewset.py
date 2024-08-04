from django.db.models import Q
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from ..models import Barbearia
from ..serializers import BarbeariaSerializer


class BarbeariaViewSet(ModelViewSet):
    queryset = Barbearia.objects.all()
    serializer_class = BarbeariaSerializer
    permission_classes = [AllowAny]
    
    filterset_fields = [
        'nome_da_barbearia'
    ]
    
    def get_queryset(self):
        import pendulum
        agora = pendulum.now().time()
        queryset = super().get_queryset()
        
        hora_de_abertura = self.request.query_params.get('hora_de_abertura')
        hora_de_fechamento = self.request.query_params.get('hora_de_fechamento')
        tipo_da_barbearia = self.request.query_params.get('tipo_da_barbearia')
        
        # if not self.request.user.is_superuser:
        #     queryset = queryset.filter(
        #         Q(dono=self.request.user) |
        #         Q(funcionarios=self.request.user)
        #     )
            
        if hora_de_abertura:
            queryset = queryset.filter(
                horario_de_abertura__lte=hora_de_abertura
            )
        elif hora_de_fechamento:
            queryset = queryset.filter(
                horario_de_fechamento__gte=hora_de_fechamento
            )
        else:
            queryset = queryset.filter(
                horario_de_abertura__lte=agora,
                horario_de_fechamento__gte=agora,
            )
        
        if tipo_da_barbearia:
            queryset = queryset.filter(tipo_de_barbearia=tipo_da_barbearia)
        
        return queryset.order_by('id')
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

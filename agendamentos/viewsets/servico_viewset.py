from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from ..models import Servico
from ..serializers import ServicoSerializer

class ServicoViewSet(ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    permission_classes = [IsAuthenticated]
    
    filterset_fields = [
        'nome_do_servico',
        'tempo_de_duracao'
    ]
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        
        servico = self.request.query_params.get('servico')
        duracao = self.request.query_params.get('duracao')
        
        if servico:
            queryset = queryset.filter(nome_do_servico__icontains=servico)
            
        if duracao:
            queryset = queryset.filter(tempo_de_duracao=duracao)
            
        return queryset
    
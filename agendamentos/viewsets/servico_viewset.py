from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

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
        preco_menor = self.request.query_params.get('preco_menor_que')
        preco_maior = self.request.query_params.get('preco_maior_que')
        
        if servico:
            queryset = queryset.filter(nome_do_servico__icontains=servico)
            
        if duracao:
            queryset = queryset.filter(tempo_de_duracao=duracao)
            
        if preco_menor:
            queryset = queryset.filter(preco__lte=preco_menor)
        
        if preco_maior:
            queryset = queryset.filter(preco__gte=preco_maior)
            
        return queryset
    
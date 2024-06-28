from rest_framework import serializers

from ..models import HistoricoDeAgendamento


class HistoricoDeAgendamentoSerializer(serializers.ModelSerializer):
    preco_total = serializers.SerializerMethodField()
    barbearia = serializers.SerializerMethodField()
    
    def get_preco_total(self, obj):
        return obj.preco_total
    
    def get_barbearia(self, obj):
        return obj.servico_fornecido.disponivel_na_barbearia.nome_da_barbearia
    
    class Meta:
        model = HistoricoDeAgendamento
        fields = '__all__'
        read_only_fields = [
            'preco_do_servico',
            'data_do_agendamento',
            'servico_fornecido',
            'cliente',
            'barbeiro'
        ]
        
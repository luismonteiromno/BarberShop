from rest_framework.serializers import ModelSerializer
from ..models import Financeiro

class FinanceiroSerializer(ModelSerializer):
    class Meta:
        model = Financeiro
        fields = '__all__'
        read_only_fields = [
            'renda_mensal',
            'despesas',
            'lucro_planos',
            'lucro_total',
            'receita_total',
            'prejuizo',
            'lucro',
            'barbearia'
        ]
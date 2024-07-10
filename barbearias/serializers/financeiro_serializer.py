from rest_framework import serializers

from ..models import Financeiro


class FinanceiroSerializer(serializers.ModelSerializer):
    barbearia = serializers.StringRelatedField()

    class Meta:
        model = Financeiro
        fields = "__all__"
        read_only_fields = [
            "renda_mensal",
            "despesas",
            "lucro_planos",
            "lucro_total",
            "receita_total",
            "prejuizo",
            "lucro",
            "barbearia",
            "lucro_mes_anterior",
            "comparar_lucros_mes_anterior_e_atual",
            "comparar_lucros_mes_anterior_e_atual_porcentagem",
        ]

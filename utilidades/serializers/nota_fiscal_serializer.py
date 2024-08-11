from rest_framework import serializers
from ..models import NotaFiscal

class NotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaFiscal
        fields = '__all__'
        read_only_fields = [
            'numero',
            'valor_total',
            'data_emissao',
            'data_vencimento',
            'produto',
            'cliente',
        ]

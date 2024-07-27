from rest_framework import serializers
from ..models import MetodoDePagamento


class MetodoDePagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoDePagamento
        fields = '__all__'

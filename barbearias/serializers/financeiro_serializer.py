from rest_framework.serializers import ModelSerializer
from ..models import Financeiro

class FinanceiroSerializer(ModelSerializer):
    class Meta:
        model = Financeiro
        fields = '__all__'
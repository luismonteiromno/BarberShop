from rest_framework.serializers import ModelSerializer

from ..models import Servico


class ServicoSerializer(ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'
        
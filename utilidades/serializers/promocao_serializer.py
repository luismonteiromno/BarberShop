from rest_framework.serializers import ModelSerializer

from ..models import Promocao


class PromocaoSerializer(ModelSerializer):
    class Meta:
        model = Promocao
        fields = '__all__'
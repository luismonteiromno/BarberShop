from rest_framework.serializers import ModelSerializer

from ..models import Barbeiro


class BarbeiroSerializer(ModelSerializer):
    class Meta:
        model = Barbeiro
        fields = '__all__'
        
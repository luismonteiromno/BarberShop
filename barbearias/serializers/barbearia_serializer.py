from rest_framework.serializers import ModelSerializer

from ..models import Barbearia


class BarbeariaSerializer(ModelSerializer):
    class Meta:
        model = Barbearia
        fields = '__all__'
        
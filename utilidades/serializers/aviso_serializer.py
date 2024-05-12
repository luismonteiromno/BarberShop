from rest_framework.serializers import ModelSerializer
from ..models import Aviso

class AvisoSerializer(ModelSerializer):
    class Meta:
        model = Aviso
        fields = '__all__'

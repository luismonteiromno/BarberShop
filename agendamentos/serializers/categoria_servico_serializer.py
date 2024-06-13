from rest_framework.serializers import ModelSerializer
from ..models import CategoriaDoServico


class CategoriaDoServicoSerializer(ModelSerializer):
    class Meta:
        model = CategoriaDoServico
        fields = '__all__'
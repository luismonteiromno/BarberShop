from rest_framework.serializers import ModelSerializer

from ..models import Avaliacao


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'
        read_only_fields = ['avaliacao', 'barbearia', 'comentario', 'usuario']
        
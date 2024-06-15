from rest_framework.serializers import ModelSerializer
from ..models import PlanosDeFidelidade

class PlanosDeFidelidadeSerializer(ModelSerializer):
    class Meta:
        model = PlanosDeFidelidade
        fields = [
            'barbearia',
            'nome',
            'cor_do_cartao',
            'beneficios',
            'preco',
            'usuarios',
        ]
        
        read_only_fields = [
            'usuarios',
        ]
        
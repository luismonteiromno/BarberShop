from rest_framework import serializers

from ..models import PlanosDeFidelidade


class PlanosDeFidelidadeSerializer(serializers.ModelSerializer):
        class Meta:
            model = PlanosDeFidelidade
            fields = [
                'id',
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
            
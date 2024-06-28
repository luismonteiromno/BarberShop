from rest_framework import serializers

from ..models import Barbearia

from decimal import Decimal


class BarbeariaSerializer(serializers.ModelSerializer):
    avisos_recentes = serializers.SerializerMethodField()
    ultimo_agendamento = serializers.SerializerMethodField()
    media_das_avaliacoes = serializers.SerializerMethodField()
    numero_de_contatos = serializers.SerializerMethodField()
    orcamento = serializers.SerializerMethodField()
    quantidade_de_agendamentos = serializers.SerializerMethodField()
    ultima_avaliacao = serializers.SerializerMethodField()

    def get_avisos_recentes(self, obj):
        aviso = obj.avisos_recentes
        return aviso if aviso else None

    def get_ultimo_agendamento(self, obj):
        ultima_agendamento = obj.ultimo_agendamento
        return str(ultima_agendamento) if ultima_agendamento else None

    def get_media_das_avaliacoes(self, obj):
        media = obj.media_das_avaliacoes_0_a_5
        return media

    def get_numero_de_contatos(self, obj):
        return obj.numero_de_contatos

    def get_orcamento(self, obj):
        return obj.orcamento

    def get_quantidade_de_agendamentos(self, obj):
        return obj.quantidade_de_agendamentos

    def get_ultima_avaliacao(self, obj):
        if obj.ultima_avaliacao:
            ultima_avaliacao = {
                "avaliacao": (
                    str(obj.ultima_avaliacao) if obj.ultima_avaliacao else None
                ),
                "comentario": (
                    str(obj.ultima_avaliacao.comentario)
                    if obj.ultima_avaliacao.comentario
                    else None
                ),
            }
        else:
            ultima_avaliacao = {
                "avaliacao": None,
                "comentario": None,
            }
        return ultima_avaliacao

    class Meta:
        model = Barbearia
        fields = "__all__"

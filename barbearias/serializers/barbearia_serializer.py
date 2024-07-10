from rest_framework import serializers
from .validators import hora_de_funcionamento
from ..models import Barbearia


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
        aviso_dicionario = {
            'aviso': str(aviso) if aviso else None,
            'descricao': str(aviso.aviso) if aviso else None,
            'data_de_inicio': str(aviso.data_de_inicio) if aviso else None,
            'data_de_encerramento': str(aviso.data_de_encerramento)
            if aviso
            else None,
        }
        return aviso_dicionario

    def get_ultimo_agendamento(self, obj):
        ultima_agendamento = obj.ultimo_agendamento
        return str(ultima_agendamento) if ultima_agendamento else None

    def get_media_das_avaliacoes(self, obj):
        return obj.media_das_avaliacoes_0_a_5

    def get_numero_de_contatos(self, obj):
        return obj.numero_de_contatos

    def get_orcamento(self, obj):
        return obj.orcamento

    def get_quantidade_de_agendamentos(self, obj):
        return obj.quantidade_de_agendamentos

    def get_ultima_avaliacao(self, obj):
        if obj.ultima_avaliacao:
            return {
                'avaliacao': str(obj.ultima_avaliacao),
                'comentario': str(obj.ultima_avaliacao.comentario)
                if obj.ultima_avaliacao.comentario
                else None,
            }
        else:
            return {
                'avaliacao': None,
                'comentario': None,
            }

    def validate_horario_de_abertura(self, value):
        abertura = self.initial_data.get('horario_de_abertura')
        fechamento = self.initial_data.get('horario_de_fechamento')
        if hora_de_funcionamento(abertura, fechamento):
            raise serializers.ValidationError(
                'Horário de abertura não pode ser maior ou igual ao horário de fechamento.'
            )
        return value

    def validate(self, attrs):
        user = self.context.get('request').user
        cnpj = attrs.get('cnpj')
        if user.is_anonymous:
            raise serializers.ValidationError(
                'É necessário estar logado para cadastrar uma barbearia.'
            )

        attrs['dono'] = user

        if Barbearia.objects.filter(cnpj=cnpj).exists():
            raise serializers.ValidationError(
                'Já existe uma barbearia com este CNPJ.'
            )

        return attrs

    class Meta:
        model = Barbearia
        fields = '__all__'
        read_only_fields = ['dono']

    def validate_cnpj(self, value):
        if value is None:
            raise serializers.ValidationError('O CNPJ é obrigatório!')
        return value

    def validate_horario_de_abertura(self, value):
        abertura = self.initial_data.get('horario_de_abertura')
        fechamento = self.initial_data.get('horario_de_fechamento')
        if value is None:
            raise serializers.ValidationError(
                'O horário de abertura é obrigatório!'
            )
        if abertura >= fechamento:
            raise serializers.ValidationError(
                'Horário de abertura não pode ser maior ou igual ao horário de fechamento.'
            )
        return value

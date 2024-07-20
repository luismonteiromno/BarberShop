from decimal import Decimal, InvalidOperation

from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg
import pendulum

from .metodo_de_pagamento import MetodoDePagamento

class Barbearia(models.Model):
    TIPO_BARBEARIA = (
        ('Própria', 'Própria'),
        ('Parceira', 'Parceira'),
        ('Locação', 'Locação'),
    )
    
    dono = models.ForeignKey(
        User,
        verbose_name='Dono',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='barbearias'
    )
    
    nome_da_barbearia = models.CharField(
        'Nome da barbearia',
        max_length=100,
        blank=True,
        null=True
    )
    
    cnpj = models.CharField(
        'CNPJ',
        max_length=19,
        blank=True,
        null=True
    )
    
    metodo_de_pagamento = models.ManyToManyField(
        MetodoDePagamento,
        verbose_name='Métodos de pagamento aceitáveis',
        blank=True
    )
    
    funcionarios = models.ManyToManyField(
        'barbearias.Funcionario',
        verbose_name='Funcionários',
        related_name='funcionario',
        blank=True
    )
    
    barbeiros = models.ManyToManyField(
        'barbearias.Barbeiro',
        verbose_name='Barbeiros',
        blank=True
    )
    
    rua = models.CharField(
        'Rua',
        max_length=100,
        blank=True,
        null=True
    )
    
    bairro = models.CharField(
        'Bairro',
        max_length=100,
        blank=True,
        null=True
    )
    
    complemento = models.CharField(
        'Complemento',
        max_length=100,
        blank=True,
        null=True
    )
    
    cidade = models.CharField(
        'Cidade',
        max_length=100,
        blank=True,
        null=True
    )
    
    estado = models.CharField(
        'Estado',
        max_length=100,
        blank=True,
        null=True
    )
    
    cep = models.CharField(
        'CEP',
        max_length=16,
        blank=True,
        null=True
    )
    
    tipo_de_barbearia = models.CharField(
        'Tipo de barbearia',
        max_length=100,
        choices=TIPO_BARBEARIA,
        blank=True,
        null=True
    )
    
    media_das_avaliacoes = models.DecimalField(
        'Média das avaliações',
        max_digits=5,
        decimal_places=1,
        blank=True,
        null=True,
        default=Decimal('0.0')
    )
    
    horario_de_abertura = models.TimeField(
        'Horário de abertura',
        blank=True,
        null=True
    )
    
    horario_de_fechamento = models.TimeField(
        'Horário de fechamento',
        blank=True,
        null=True
    )
    
    data_de_criacao = models.DateTimeField(
        'Data de criação',
        auto_now_add=True,
        blank=True,
        null=True
    )
    
    data_de_atualizacao = models.DateTimeField(
        'Data de atualização',
        auto_now=True,
        blank=True,
        null=True
    )
    
    usuario_de_criacao = models.ForeignKey(
        User,
        verbose_name='Usuário de criação',
        related_name='usuario_criacao',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    usuario_de_atualizacao = models.ForeignKey(
        User,
        verbose_name='Usuário de atualização',
        related_name='usuario_atualizacao',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    @property
    def orcamento(self):
        orcamento = self.financeiro.lucro_total
        if orcamento:
            return orcamento
        else:
            return 0

    @property
    def quantidade_de_agendamentos(self):
        from datetime import datetime

        from agendamentos.models import Agendamento

        if self.pk:
            agendamentos = Agendamento.objects.filter(
                data_marcada__gt=datetime.now(),
                servico__disponivel_na_barbearia=self.pk,
            ).count()
            return agendamentos
        else:
            return 0

    @property
    def numero_de_contatos(self):
        contatos = self.contatos.all().count()
        return contatos

    @property
    def ultimo_agendamento(self):
        from agendamentos.models import Agendamento

        if self.pk:
            agendamento = (
                Agendamento.objects.filter(servico__disponivel_na_barbearia=self.pk)
                .select_related("servico")
                .last()
            )
            if agendamento:  
                if (
                    agendamento.data_marcada.date().day - pendulum.now().day
                ) == 2:
                    return None
            return agendamento
        else:
            return None

    @property
    def avisos_recentes(self):
        if self.pk:
            avisos = self.aviso_set.order_by("-data_de_inicio").last()
            return avisos
        else:
            return None

    @property
    def media_das_avaliacoes_0_a_5(self):
        media = self.avaliacao_set.aggregate(media_avaliacao=Avg("avaliacao"))["media_avaliacao"]
        if media:
            return Decimal(media).quantize(Decimal("0.0"))
        else:
            return Decimal(0.0)

    @property
    def ultima_avaliacao(self):
        ultima_avaliacao = self.avaliacao_set.last()
        return ultima_avaliacao

    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.pk:
            self.dono = user
            self.usuario_de_criacao = user
        else:
            self.dono = user
            self.usuario_de_atualizacao = user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_da_barbearia

    class Meta:
        verbose_name = "Barbearia"
        verbose_name_plural = "Barbearias"

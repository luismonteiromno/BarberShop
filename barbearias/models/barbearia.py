from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg


class Barbearia(models.Model):
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
    
    funcionarios = models.ManyToManyField(
        User,
        verbose_name='Funcionários',
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
    
    @property
    def quantidade_de_agendamentos(self):
        from agendamentos.models import Agendamento
        if self.pk:
            agendamentos = Agendamento.objects.filter(
                servico__disponivel_na_barbearia=self.pk
            ).select_related('servico').count()
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
            agendamentos = Agendamento.objects.filter(
                servico__disponivel_na_barbearia=self.pk
            ).select_related('servico').last()
            return agendamentos
        else:
            return None
        
    @property
    def avisos_recentes(self):
        if self.pk:
            avisos = self.aviso_set.order_by('-data_de_inicio').last()
            return avisos
        else:
            return None
        
    @property
    def media_das_avaliacoes(self):
        media = self.avaliacao_set.all()
        if media:
            media = media.aggregate(Avg('avaliacao'))['avaliacao__avg']
            return media
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.pk:
            self.dono = user    
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.nome_da_barbearia
    
    class Meta:
        verbose_name = 'Barbearia'
        verbose_name_plural = 'Barbearias'
    
    
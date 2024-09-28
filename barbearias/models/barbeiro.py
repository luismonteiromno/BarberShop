from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg

from .barbearia import Barbearia


class Barbeiro(models.Model):
    barbeiro = models.ForeignKey(
        User,
        verbose_name='Barbeiro',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='barbeiro'
    )
    
    servicos = models.ManyToManyField(
        'agendamentos.Servico',
        verbose_name='Serviços',
        blank=True,
    )
    
    barbearias = models.ManyToManyField(
        Barbearia,
        verbose_name='Barbearia que o barbeiro trabalha',
    )
    
    salario = models.DecimalField(
        'Salário',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    
    freelancer =  models.BooleanField(
        'Barbeiro Freelancer',
        default=False
    )
    
    avaliacao = models.DecimalField(
        'Avaliação do barbeiro',
        max_digits=5,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        blank=True,
        null=True,
    )
    
    @property
    def media_avaliacoes(self):
        from decimal import Decimal
        media = self.barbeiro_avaliacao.aggregate(media=Avg('avaliacao'))['media']
        if media:
            return Decimal(media).quantize(Decimal('0.00'))
        else:
            return Decimal('0.00')
    
    def save(self, *args, **kwargs):
        self.avaliacao = self.media_avaliacoes
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.barbeiro)
    
    class Meta:
        verbose_name = 'Barbeiro'
        verbose_name_plural = 'Barbeiros'
        
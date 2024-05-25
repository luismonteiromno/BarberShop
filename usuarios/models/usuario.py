from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    TYPE_USER = (
        ('Barbeiro', 'Barbeiro'),
        ('Cliente', 'Cliente'),
    )
    
    usuario = models.OneToOneField(
        User,
        verbose_name='Usuário',
        on_delete=models.CASCADE
    )
    
    tipo_do_usuario = models.CharField(
        max_length=10,
        choices=TYPE_USER,
        verbose_name='Tipo de Usuário',
        default='Cliente',   
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.usuario)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
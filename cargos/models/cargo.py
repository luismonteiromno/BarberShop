from django.db import models

class Cargo(models.Model):
    nome_do_cargo = models.CharField(
        max_length=100,
        verbose_name='Nome do Cargo'
    )
    
    nivel_hierarquico = models.CharField(
        max_length=100,
        verbose_name='Nível hierárquico',
        choices=[
            ('Gerente', 'Gerente'),
            ('Diretor', 'Diretor'),
            ('Supervisor', 'Supervisor'),
            ('Colaborador', 'Colaborador'),
        ]
    )
    
    @property
    def funcionarios_com_esse_cargo(self):
        return self.funcionario_set.all().count()
    
    def __str__(self):
        return self.nome_do_cargo
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
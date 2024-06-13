from django.db import models

class CategoriaDoServico(models.Model):
    
    nome = models.CharField(
        'Nome',
        max_length=100,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Categoria do Serviço'
        verbose_name_plural = 'Categorias dos Serviços'
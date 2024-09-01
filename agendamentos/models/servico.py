from datetime import datetime

from django.db import models
from django_editorjs import EditorJsField
from tinymce.models import HTMLField

from barbearias.models import Barbearia

from .categoria_servico import CategoriaDoServico


class Servico(models.Model):
    disponivel_na_barbearia = models.ForeignKey(
        Barbearia,
        verbose_name='Barbearia',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
  
    nome_do_servico = models.CharField(
        'Nome do serviço',
        max_length=100,
        blank=True,
        null=True
    )
    
    descricao = HTMLField(
        verbose_name='Descrição',
        blank=True,
        null=True,
        help_text='Você também pode adicionar imagens na descrição',
        # editorjs_config={
        #   "tools": {
        #     "Table": {
        #       "disabled": True,
        #     },
        #     "Image": {
        #       "config": {
        #         "endpoints": {
        #           "byFile": '/imageUpload/',
        #           "byUrl": '/imageUpload/',
        #         },
        #         "additionalRequestHeaders": [
        #           {"Content-Type": "multipart/form-data"}
        #         ]
        #       },
        #     },
        #     "Attaches": {
        #       "disabled": True,
        #       "config": {
        #         "endpoint": '/fileUpload/',
        #       },
        #     },
        #     "Quote": {
        #       "disabled": True,
        #     },
        #     "Link": {
        #       "disabled": True,
        #     },
        #     "Raw": {
        #       "disabled": True,
        #     },
        #   }
        # }
    )
    
    categoria = models.ForeignKey(
       CategoriaDoServico,
       verbose_name='Categoria',
       on_delete=models.SET_NULL,
       blank=True,
       null=True,
    )
    
    tempo_de_duracao_minutos = models.PositiveIntegerField(
        'Tempo de Duração (em minutos)',
        blank=True,
        null=True
    )
    
    preco = models.DecimalField(
        'Preço',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    
    @property
    def ultima_promocao(self):
        promocao = self.promocao_set.order_by('-inicio_da_promocao').last()
        if promocao:
           return promocao
        else:
            return None
          
    @property
    def promocao_atual(self):
        promocao = (
          self.promocao_set.filter(
            inicio_da_promocao__lte=datetime.now().date(),
            fim_da_promocao__gte=datetime.now().date()
          )
          .order_by('-inicio_da_promocao')
          .last()
        )
        if promocao:
            return promocao
        else:
            return 'Nenhuma promoção no momento'
      
    
    def __str__(self):
        return self.nome_do_servico
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    
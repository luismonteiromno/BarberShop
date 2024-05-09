from django.db import models
from django_editorjs import EditorJsField
from barbearias.models import Barbearia

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
    
    descricao = EditorJsField(
        verbose_name='Descrição',
        blank=True,
        null=True,
        help_text='Você também pode adicionar imagens na descrição',
        editorjs_config={
          "tools": {
            "Table": {
              "disabled": True,
            },
            "Image": {
              "config": {
                "endpoints": {
                  "byFile": '/imageUpload/',
                  "byUrl": '/imageUpload/',
                },
                "additionalRequestHeaders": [
                  {"Content-Type": "multipart/form-data"}
                ]
              },
            },
            "Attaches": {
              "disabled": True,
              "config": {
                "endpoint": '/fileUpload/',
              },
            },
            "Quote": {
              "disabled": True,
            },
            "Link": {
              "disabled": True,
            },
            "Raw": {
              "disabled": True,
            },
          }
        }
    )
    
    tempo_de_duracao = models.TimeField(
        'Tempo de duração',
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
    
    def __str__(self):
        return self.nome_do_servico
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    
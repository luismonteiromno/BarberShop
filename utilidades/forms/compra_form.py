from django import forms

from ..models import Produto


class CompraForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        produto = cleaned_data.get('produto')
        quantidade_do_produto = produto.quantidade
        quantidade = cleaned_data.get('quantidade')
        if quantidade > quantidade_do_produto:
            raise forms.ValidationError(
                f'Quantidade ultrapassa a quantidade disponivel no estoque!. Quantidade no estoque: {quantidade_do_produto}'
            )

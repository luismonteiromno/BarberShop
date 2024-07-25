from django import forms
from ..models import ChavePix


class ChavePixForm(forms.ModelForm):
    
    def clean(self):
        cleaned_data = super().clean()
        cpf_cnpj = cleaned_data.get('cpf_cnpj')
        telefone = cleaned_data.get('telefone')
        
        if cpf_cnpj >= 1:
            raise forms.ValidationError('Você já possui um CPF/CNPJ como chave PIX cadastrada.')
        
        if telefone >= 1:
            raise forms.ValidationError('Você já possui um telefone como chave PIX cadastrada.')
        
        return cleaned_data

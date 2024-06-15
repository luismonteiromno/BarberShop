from django import forms
from ..models import Agendamento

class AgendamentoForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        data_marcada = cleaned_data.get('data_marcada')
        servico = cleaned_data.get('servico')
        ...
        if not servico:
            raise forms.ValidationError('Escolha um serviço!')
        
        if not data_marcada:
            raise forms.ValidationError('Escolha uma data!')
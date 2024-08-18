from django import forms


class AvisoForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get('data_de_inicio')
        encerramento = cleaned_data.get('data_de_encerramento')

        if (inicio is not None and encerramento is not None) and (
            inicio >= encerramento
        ):
            raise forms.ValidationError(
                'A data de encerramento deve ser maior que a data de início'
            )
        else:
            raise forms.ValidationError(
                'Preencha os campos de data corretamente seu comédia!'
            )

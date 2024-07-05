from rest_framework import serializers

def hora_de_funcionamento(abertura, fechamento):
    if abertura >= fechamento:
        raise serializers.ValidationError(
            'Horário de abertura não pode ser maior ou igual ao horário de fechamento.'
        )
        

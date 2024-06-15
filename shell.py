from barbearias.models import Cliente
from django.contrib.auth.models import User

users = User.objects.all()
for user in users:
    cliente = User.objects.get(pk=user.id)
    if not cliente:
        Cliente.objects.create(
            cliente=user,
        )
        print(f'usuario {user} criado')
    else:
        print(f'usuario {user} ja existe')
        
from agendamentos.models import MeuAgendamento, Agendamento

agendamentos = Agendamento.objects.all().delete()
meus_agendamentos = MeuAgendamento.objects.all().delete()
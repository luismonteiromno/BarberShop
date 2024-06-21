from django.contrib.auth.models import User

from barbearias.models import Cliente

users = User.objects.all()
for user in users:
    cliente = User.objects.get(pk=user.id)
    if not cliente:
        Cliente.objects.create(
            cliente=user,
        )
        print(f"usuario {user} criado")
    else:
        print(f"usuario {user} ja existe")

from agendamentos.models import Agendamento, MeuAgendamento

agendamentos = Agendamento.objects.all().delete()
meus_agendamentos = MeuAgendamento.objects.all().delete()

# teste = dict(teste=1, teste2=2)
# teste = dict(zip(['teste', 'teste2'], [1, 2]))

# filtros = {}
# if barbearia:
#     filtros['nome'] = barbearia.nome_da_barbearia
# print(filtros)
# print("nome: {nome}".format(**filtros))

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

from barbearias.models import Barbearia

barbearia = Barbearia.objects.first()
print(barbearia.orcamento)

from barbearias.crons import AtualizarFinancasCronJob
job = AtualizarFinancasCronJob()
job.do()



from barbearias.models import Barbearia

Barbearia.objects.bulk_create([
    Barbearia(
        nome_da_barbearia='Barbershop',
        cnpj='12345678901234',
        rua='Rua 1',
        bairro='Bairro A',
        complemento='',
        cidade='Cidade A',
        estado='SP',
        cep='00000-000',
        tipo_de_barbearia='Loja Própria',
        horario_de_abertura='08:00',
        horario_de_fechamento='21:00',
        dono=None
    ),
    Barbearia(
        nome_da_barbearia='Barbershop 2',
        cnpj='98765432109876',
        rua='Rua Teste 2, 456',
        bairro='Bairro B',
        complemento='',
        cidade='Cidade B',
        estado='RJ',
        cep='11111-111',
        tipo_de_barbearia='Loja Própria',
        horario_de_abertura='08:00',
        horario_de_fechamento='21:00',
        dono=None
    ),
    Barbearia(
        nome_da_barbearia='Barbershop 3',
        cnpj='12345678901234',
        rua='Rua Teste 3, 789',
        bairro='Bairro C',
        complemento='',
        cidade='Cidade C',
        estado='MG',
        cep='22222-222',
        tipo_de_barbearia='Loja Própria',
        horario_de_abertura='08:00',
        horario_de_fechamento='21:00',
        dono=None
    )
])

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

from barbearias.crons import AtualizarClienteCronJob, AtualizarFinancasCronJob
job = AtualizarFinancasCronJob()
job.do()

credito = AtualizarClienteCronJob()
credito.do()

from barbearias.models import Financeiro
financeiro = Financeiro.objects.get(id=1)
financeiro.renda_mensal,  = 0
financeiro.lucro_mes_anterior = 0
financeiro.despesas = 0
financeiro.comparar_lucros_mes_anterior_e_atual = 0
financeiro.lucro_planos = 0
financeiro.lucro_total = 0
financeiro.receita_total = 0
financeiro.prejuizo, financeiro.lucro = False

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
        dono_id=1
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
        dono_id=1
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
        dono_id=1
    )
])


# limpar financeiros

from barbearias.models import Financeiro, Avaliacao

financeiro = Financeiro.objects.filter(barbearia__isnull=True)
financeiro.delete()


from agendamentos.models import Agendamento
from barbearias.models import Barbeiro, Barbearia


barbearia = Barbearia.objects.all()
barbeiros = Barbeiro.objects.prefetch_related('barbearias').all()
for i in barbeiros:
    print(i)
...

# Metódos de iteração
from functools import reduce

array = [1, 2, 3, 4 ,5]

print(reduce(lambda x, y: x+y*2, array))
print(list(map(lambda x: x*2, array)))
print(list(filter(lambda x: x>2, array)))

from django.db.models.utils import list_to_queryset
from barbearias.models import *

# Querysets
barbearias = Barbearia.objects.all()
barbearias_filtradas = barbearias.filter(nome_da_barbearia__contains='Barbershop')
barbearias_ordenadas = barbearias_filtradas.order_by('nome_da_barbearia')
barbearias_paginadas = barbearias_ordenadas.paginate(page=1, per_page=10)
barbearias_list = list_to_queryset(barbearias_paginadas.object_list)
print(barbearias_list)

import pendulum
from django_cron import CronJobBase, Schedule

from ..models import Agendamento


class AtualizarAgendamentosCronJob(CronJobBase):
    RUN_AT_TIMES = ['00:00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)

    code = 'agendamentos.atualizar_agendamentos'

    def do(self):
        hoje = pendulum.now()
        agendamentos = Agendamento.objects.filter(
            data_marcada__lte=hoje, passou_da_data=False
        )
        for agendamento in agendamentos:
            agendamento.passou_da_data = True
            agendamento.save()

from django_cron import Schedule, CronJobBase

from barbearias.models.financeiro import Financeiro
from ..models import Barbearia
import logging

logger = logging.getLogger(__name__)


class AtualizarFinancasCronJob(CronJobBase):
    RUN_EVERY_MINS = 10  # every 10 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    code = "barbearias.atualizar_financas"

    def do(self):
        barbearias = Barbearia.objects.all()
        for barbearia in barbearias:
            Financeiro().atualizar_financas(self, barbearia)

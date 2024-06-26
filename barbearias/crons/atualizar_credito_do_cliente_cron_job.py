from django_cron import CronJobBase, Schedule

from ..models import Cliente


class AtualizarClienteCronJob(CronJobBase):
    RUN_AT_TIMES = ['00:00'] 
    
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    
    code = "barbearias.atualizar_cliente"
    
    def do(self):
        clientes = Cliente.objects.all()
        for cliente in clientes:
            Cliente().atualizar_credito_cliente(cliente)
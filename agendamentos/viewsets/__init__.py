from .agendamento_viewset import AgendamentoViewSet
from .categoria_servico_viewset import CategoriaDoServicoViewSet
from .historico_agendamento_viewset import HistoricoDeAgendamentoViewSet
from .meu_agendamento_viewset import MeuAgendamentoViewSet
from .servico_viewset import ServicoViewSet

__all__ = [
    AgendamentoViewSet,
    CategoriaDoServicoViewSet,
    HistoricoDeAgendamentoViewSet,
    MeuAgendamentoViewSet,
    ServicoViewSet
]
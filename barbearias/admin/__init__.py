from .avaliacao_admin import AvaliacaoAdmin
from .barbearia_admin import BarbeariaAdmin
from .barbeiro_admin import BarbeiroAdmin
from .cliente_admin import ClienteAdmin
from .contato_inline import ContatoInline
from .cliente_inline import ClienteInline
from .financeiro_admin import FinanceiroAdmin
from .plano_fidelidade_admin import PlanosDeFidelidadeAdmin

__all__ = [
    AvaliacaoAdmin,
    BarbeariaAdmin,
    BarbeiroAdmin,
    ClienteAdmin,
    ContatoInline,
    ClienteInline,
    FinanceiroAdmin,
    PlanosDeFidelidadeAdmin,
]
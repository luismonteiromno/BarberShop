from .avaliacao_admin import AvaliacaoAdmin
from .avaliacao_barbeiro_admin import AvaliacaoDoBarbeiroAdmin
from .barbearia_admin import BarbeariaAdmin
from .barbeiro_admin import BarbeiroAdmin
from .cliente_admin import ClienteAdmin
from .cliente_inline import ClienteInline
from .contato_inline import ContatoInline
from .financeiro_admin import FinanceiroAdmin
from .funcionario_admin import FuncionarioAdmin
from .funcionario_inline import FuncionarioInline
from .plano_fidelidade_admin import PlanosDeFidelidadeAdmin

__all__ = [
    AvaliacaoAdmin,
    AvaliacaoDoBarbeiroAdmin,
    BarbeariaAdmin,
    BarbeiroAdmin,
    ClienteAdmin,
    ContatoInline,
    ClienteInline,
    FinanceiroAdmin,
    FuncionarioAdmin,
    FuncionarioInline,
    PlanosDeFidelidadeAdmin,
]
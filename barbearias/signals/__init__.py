from .signal_registrar_cliente import registrar_cliente
from .signal_registrar_funcionario import registrar_funcionario
from .signal_registrar_lucros_barbearia import (
    # atualizar_lucros, 
    registrar_lucros
)

__all__ = [
    # 'atualizar_lucros',
    'registrar_cliente',
    'registrar_funcionario',
    'registrar_lucros',
]
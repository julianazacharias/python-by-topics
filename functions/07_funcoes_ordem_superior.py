"""HOFs."""
from typing import Callable, Any

soma_2 = lambda val: val + 2


# Twice
def reaplica(func: Callable, val: Any) -> Any:
    """Função que reaplica a função ao resultado da chamada."""
    return func(func(val))


def seleciona(op: str) -> Callable:
    """Seleciona uma função, usando seu nome."""
    ops = {
        'soma': lambda x, y: x + y,
        'sub': lambda x, y: x - y
    }
    return ops[op]


palavras = [
    'amar', 'transar', 'falar', 'abacaxi', 'xixi', 'chute'
]

def take_cond(func, valores):
    for val in valores:
        if func(val):
            yield val
        else:
            break

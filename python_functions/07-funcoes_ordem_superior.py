"""HOFs. High order functions."""

# É UMA FUNÇÃO QUE RECEBE UMA FUNÇÃO,
# É UMA FUNÇÃO QUE RETORNA UMA FUNÇÃO E
# É UMA FUNÇÃO QUE RECEBE E RETORNA UMA FUNÇÃO

from typing import Callable, Any
from itertools import takewhile

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

# seleciona(soma)(5, 10)
# seleciona(sub)(4, 2)


palavras = [
    'amar', 'transar', 'falar', 'abacaxi', 'xixi', 'chute'
]

#sorted(palavras)
#sorted(palavras, key=lambda uma_string: uma_string[1])  #ordenando a partir da posição 1 (segunda posição)

#list(map(lambda val: val*2, palavras))

def take_cond(func, valores):
    for val in valores:
        if func(val):
            yield val
        else:
            break

list(takewhile(lambda x: x < 10, [8, 9, 10, 11])) # enquanto x for menor que 10, vai imprimindo os nums da lista
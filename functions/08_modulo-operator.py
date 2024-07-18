"""Operator."""
from operator import (
    add, mul, sub, itemgetter
)
from functools import reduce

reduce(add, [1, 2, 3, 4, 5])
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
reduce(sub, [1, 2, 3, 4, 5])
reduce(mul, [1, 2, 3, 4, 5])

palavras = [
    'amar', 'transar', 'falar', 'abacaxi', 'xixi', 'chute'
]

sorted(palavras, key=lambda string: string[1])
sorted(palavras, key=itemgetter(1))

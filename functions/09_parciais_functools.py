"""Funções parciais."""
from operator import add, mul, itemgetter
from functools import partial, reduce

soma_2 = partial(add, 2)
mul_2 = partial(mul, 2)

reduce(add, [1, 2, 3, 4, 5])  # Somatório
reduce(mul, [1, 2, 3, 4, 5])  # mul

somatorio = partial(reduce, add)
multiplicatio = partial(reduce, mul)
mul_2_all = partial(map, mul_2)
ordenar_1 = partial(sorted, key=itemgetter(1))


def func(b, c, d, e, database=None):
    return database, b, c, d, e


func_postgres = partial(func, database='postgres')
func_maria = partial(func, database='mariaDB')
func_mongo = partial(func, database='mongDB')

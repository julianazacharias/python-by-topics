"""Des|empacotamento de argumentos."""

# **************** EMPACOTAMENTO ****************

# def meu_sum(*args, **kwargs):
def meu_sum(*grupo_posicional, **grupo_nomeado):
    """Empacotamento."""
    print(grupo_posicional, grupo_nomeado)
    print(type(grupo_posicional), type(grupo_nomeado))
    return grupo_posicional, grupo_nomeado

# *grupo_posicional é uma TUPLA <class 'tuple'>
# **grupo_nomeado é um DICIONARIO <class 'dict'>




# **************** DESEMPACOTAMENTO ****************

lista = [-1, 2, 3, 4, -10]


def meu_min(a, b, c, d, *args):
    return min((a, b, c, d, *args)) #minimo valor da lista  é -10

# meu_mim(*lista)

dicionario = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}


def meu_max(a=0, b=0, c=0, d=0):
    return max((a, b, c, d)) #maximo valor da lista  é 4


# meu_max(**dicionario)

l = [1, 2, 3]
d = {'d': 4, 'e': 5}


def meu_mix(a, b, c, d=0, e=0):
    return a, b, c, d, e

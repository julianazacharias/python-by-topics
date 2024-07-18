"""Des|empacotamento de argumentos."""


# def meu_sum(*args, **kwargs):
def meu_sum(*grupo_pos, **grupo_nomeado):
    """Empacotamento."""
    print(grupo_pos, grupo_nomeado)
    print(type(grupo_pos), type(grupo_nomeado))
    return grupo_pos, grupo_nomeado


lista = [-1, 2, 3, 4, -10]


def meu_mim(a, b, c, d, *args):
    return min((a, b, c, d, *args))

# meu_mim(*lista)

dicionario = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}


def meu_max(a=0, b=0, c=0, d=0):
    return max((a, b, c, d))


# meu_max(**dicionario)

l = [1, 2, 3]
d = {'d': 4, 'e': 5}


def meu_mix(a, b, c, d=0, e=0):
    return a, b, c, d, e

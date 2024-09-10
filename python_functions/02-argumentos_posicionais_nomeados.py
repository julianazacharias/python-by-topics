funcao_anonima = lambda parametro : parametro + 2

funcao_anonima_plus = lambda parametro1, parametro2 : parametro1 + parametro2

def soma_posicional(x, y):
    """X e Y são parametros posicionais."""
    return x + y


def soma_nomeados(x=7, y=7):
    """
    X e Y são parametros nomeados.

    na falta de x ou y, o valor 7 será usado
    """
    print(f'x: {x}, y:{y}')
    return x + y


def soma_explicitamente_nomeados(*, x=7, y=7):
    """
    X e Y são parametros nomeados.

    na falta de x ou y, o valor 7 será usado
    """
    print(f'x: {x}, y:{y}')
    return x + y


def soma_explicitamente_nomeados2(x=7, *, y=7):
    """
    X e Y são parametros nomeados.

    na falta de x ou y, o valor 7 será usado
    """
    print(f'x: {x}, y:{y}')
    return x + y


def soma_explicitamente_posicionais(x, y, /):
    """
        X e Y são parametros posicionais.

    """
    print(f'x: {x}, y:{y}')
    return x + y


def suma_tudo_mix(x, y, /, z, *, w):
    """
        X e Y são estritamente posicionais, 
        Z como misto e 
        Z estritamente nomeado.
        (1, 2, 3, w=1) ou
        (1, 2, z=3, w=1)

    """
    return sum((x, y, z, w))

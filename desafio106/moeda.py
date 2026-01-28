def moeda(valor=0, simbolo='R$'):
    return f'{simbolo}{valor:.2f}'.replace('.', ',')


def dobro(n=0, format=False):
    resultado = n * 2
    return moeda(resultado) if format else resultado


def metade(n=0, format=False):
    resultado = n / 2
    return moeda(resultado) if format else resultado


def aumentar(n=0, taxa=0, format=False):
    resultado = n + (n * taxa / 100)
    return moeda(resultado) if format else resultado


def diminuir(n=0, taxa=0, format=False):
    resultado = n - (n * taxa / 100)
    return moeda(resultado) if format else resultado

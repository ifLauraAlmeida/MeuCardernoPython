def moeda(valor=0, simbolo='R$'):
    return f'{simbolo}{valor:.2f}'.replace('.', ',')


def dobro(p=0, format=False):
    resultado = p * 2
    return moeda(resultado) if format else resultado


def metade(p=0, format=False):
    resultado = p / 2
    return moeda(resultado) if format else resultado


def aumentar(p=0, taxa=0, format=False):
    resultado = p + (p * taxa / 100)
    return moeda(resultado) if format else resultado


def diminuir(p=0, taxa=0, format=False):
    resultado = p - (p * taxa / 100)
    return moeda(resultado) if format else resultado

def resumo(p=0,taxa_a=10,taxa_b=20):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p,True)}')
    print(f'Metade do preco: \t{metade(p,True)}')
    print(f'{taxa_a}% de aumento: \t{aumentar(p,taxa_a,True)}')
    print(f'{taxa_b}% de redução: \t{diminuir(p,taxa_b,True)}')

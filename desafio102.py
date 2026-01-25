#Exercício Python 102: Crie um programa 
# que tenha uma função fatorial() que 
# receba dois parâmetros: o primeiro 
# que indique o número a calcular e outro
# chamado show, que será um valor lógico
# (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo 
# do fatorial.

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: número a ser calculado
    :param show: (opcional) mostra ou não o processo do cálculo
    :return: o valor do fatorial de n
    """
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c, end=' x ' if c > 1 else ' = ')
        f *= c
    return f

print(fatorial(5,show=False))
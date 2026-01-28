def dobro(n):
    resultado = n * 2
    return resultado
def metade(n):
    resultado = n / 2
    return resultado
def aumentar(n):
    resultado = n + (n * 0.1)
    return resultado
def diminuir(n):
    resultado = n - (n * 0.1)
    return resultado
def moeda(valor=0, simbolo='R$'):
    return f'{simbolo}{valor:.2f}'.replace('.',',')

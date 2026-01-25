#Exercício Python 100: Faça um programa que tenha 
#uma lista chamada números e duas funções chamadas 
#sorteia() e somaPar(). A primeira função vai 
#sortear 5 números e vai colocá-los dentro da lista
#e a segunda função vai mostrar a soma entre todos 
#os valores pares sorteados pela função anterior.

from random import sample

def sorteia(*num):
    sorteados = 0
    print(f'Sorteando valores da lista: ', end=' ')
    sorteados = sample(num,5)
    print(f'{sorteados} PRONTO!')
    return sorteados
    
def somaPar(*num):
    sorteados = sorteia(*num)
    soma = 0
    for i in sorteados:
        if i % 2 == 0:
            soma += i
    print(f'Soma dos pares: {soma}')

#Programa Principal

somaPar(1,2,3,4,5,6,7,8,9,10)
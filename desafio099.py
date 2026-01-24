#Exercício Python 099: Faça um programa que tenha
#uma função chamada maior(), que receba vários 
#parâmetros com valores inteiros. Seu programa 
#tem que analisar todos os valores e dizer qual 
#deles é o maior.


def maior(*num):
    if not num:
        print('Nenhum valor informado.')
        return
    print('Analisando os valores passados...')
    print(*num)
    print(f'O maior valor informado foi {max(num)}')
def divisoria():
    print('-='*30)

#Programa Principal
maior(2,9,4,5,7,1)
divisoria()
maior(4,7,0)
divisoria()
maior(1,2)
divisoria()
maior(6)
divisoria()
maior()
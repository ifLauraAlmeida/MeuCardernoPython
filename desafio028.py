#Escreva um programa que faça o computador "pensar" em um número inteiro e entre 0 e 5 e peça
#para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá imprimir se o usuário venceu ou perdeu.

import random as rd

num = rd.randint(0,5)
num_usuario = int(input('Estou pensando em um número de 0 a 5. Tente adivinhar... '))
if num_usuario == num:
    print('VOCÊ ACERTOU BROTHER!')
else:
    print('ERROU COLEGA')
print(f"O número pensado foi {num}.")
print('--FIM--')
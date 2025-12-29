# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint

computador = 0
jogador = 0
print('''Suas opções:
[ 1 ] ÍMPAR
[ 2 ] PAR
''')

jogador = int(input('Qual a sua jogada? '))

# computador escolhe o oposto
if jogador == 1:
    jogador = "Ímpar"
    computador = "Par"
else:
    jogador = "Par"
    computador = "Ímpar"

print('-=' * 20)
print(f'Jogador escolheu {jogador}')
print(f'Computador ficou com {computador}')
print('-=' * 20)

num_jogador = int(input("Escolha um número de 1 a 10: "))
num_computador = rd.randint(0,11)



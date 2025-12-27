#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint as rd
itens = ('Pedra', 'Papel', 'Tesoura')
computador = rd(0,2)
print ('''Suas opções:
       [ 0 ] PEDRA
       [ 1 ] PAPEL
       [ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada?'))
print('-=' * 10)
print(f'O computador escolheu {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 10)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    else:
        print('JOGADOR PERDE')
elif computador == 1:
    if jogador == 0:
        print('JOGADOR PERDE')
    elif jogador == 1:
        print('EMPATE')
    else:
        print('JOGADOR VENCE')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('JOGADOR PERDE')
    else:
        print('EMPATE')


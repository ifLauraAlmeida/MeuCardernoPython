# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint as rd

itens = ('Ímpar', 'Par')
computador = rd(1,2)
universo = rd(1,)
print ('''Suas opções:
       [ 1 ] ÍMPAR
       [ 2 ] PAR''')
jogador = int(input('Qual a sua jogada?'))
print('-=' * 20)
print(f'O computador escolheu {itens[computador-1]}')
print(f'Jogador jogou {itens[jogador-1]}')
print('-=' * 20)


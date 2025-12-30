# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

import random as rd

computador = 0
jogador = 0
vitorias = 0

while True:
    print('''Suas opções:
    [ 1 ] ÍMPAR
    [ 2 ] PAR
    ''')
    jogador = int(input('Qual a sua jogada? '))

    if jogador == 1: # aqui o computador escolherá sempre o oposto dando prioridade para o usuário
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
    num_computador = rd.randint(0,11) # aqui o pc escolhe um número de 1 a 10
    print("-="*20)
    print(f"Você escolheu {num_jogador}.")
    print(f"O Computador escolheu {num_computador}.")
    resultado = num_jogador + num_computador
    print(f"{num_jogador} + {num_computador} = {resultado}")
    print("-="*20)

    print(f"LOGO:")

    if resultado / 2 == 0:
        print(f"{resultado} É ÍMPAR")
        if jogador == "Ímpar":
            print("Jogador venceu!")
            vitorias += 1
        else:
            print("Computador venceu")
            break
    else:
        print(f"{resultado} É PAR")
        if jogador == "Par":
            print('Jogador venceu!')
            vitorias += 1
        else:
            print("Computador venceu!")
            break
print(f"Você venceu {vitorias} vezes.")

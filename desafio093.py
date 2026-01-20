#Exercício Python 093: Crie um programa que gerencie o aproveitamento 
#de um jogador de futebol. O programa vai ler o nome do jogador e 
#quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos 
#em cada partida. No final, tudo isso será guardado em um dicionário, 
#incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()

jogador['nome'] = str(input('Nome do candango: '))
jogador['partidas'] = int(input('Quantas partidas? '))

if jogador['partidas'] != 0:
    for c in range(jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {c + 1}: ')))
        print(gols)

#Exercício Python 093: Crie um programa que gerencie o aproveitamento 
#de um jogador de futebol. O programa vai ler o nome do jogador e 
#quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos 
#em cada partida. No final, tudo isso será guardado em um dicionário, 
#incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()

jogador['nome'] = str(input('Nome do candango: ')).title()
jogador['partidas'] = int(input('Quantas partidas? '))


for c in range(jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {c + 1}: ')))
jogador['total'] = sum(gols)
jogador['goals'] = gols
print()

print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}. ')
print('-='*30)
print(f'O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.')
for k in range(len(gols)):
    print(f'   => Na partida {k}, fez {gols[k]} gols.')
print(f'Foi um total de {jogador['total']}')



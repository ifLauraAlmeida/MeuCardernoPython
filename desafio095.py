#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
jogadores = list()
gols = list()

while True:
    jogador['nome'] = str(input('Nome: ')).title()
    jogador['partidas'] = int(input('Quantas partidas? '))
    
    for c in range(jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
        
    jogador['total'] = sum(gols)
    jogador['goals'] = gols
    jogadores.append(jogador)
    print(jogadores)
    
    resp = str(input('Deseja prosseguir [S/N]? ')).upper()[0]
    if resp == 'N':
        break

    
    for k in range
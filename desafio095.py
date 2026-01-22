#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
jogadores = list()
gols = list()

jogador = {}
jogadores = []
gols = []

while True:
    jogador.clear()
    gols.clear()

    jogador['nome'] = str(input('Nome: ')).title()
    jogador['partidas'] = int(input('Quantas partidas? '))
    
    for c in range(jogador['partidas']):
        gols.append(int(input(f'   Quantos gols na partida {c+1}: ')))
        
    jogador['total'] = sum(gols)
    jogador['gols'] = gols.copy()
    jogadores.append(jogador.copy())
    
    resp = str(input('=>Deseja prosseguir [S/N]? ')).upper()[0]
    if resp == 'N':
        break
    
print('-=' * 30)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"total":<5}')
print('-' * 40)

for i,j in enumerate(jogadores):
    print(f'{i:<4}{j['nome']:<15}{str(j['gols']):<15}{j['total']:<5}')
    
while True:
    busca = int(input('\nMostrar dados de qual jogador (999 para parar)? '))
    if busca == 999:
        break
    if busca < 0 or busca >= len(jogadores):
        print('Jogador não encontrado.')
    else:
        print('\033[1m => LEVANTAMENTO JOGADOR\033[m')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')

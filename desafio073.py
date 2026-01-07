# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados 
# da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Santos.

times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 
'Fluminense', 'Vasco', 'Bragantino', 'Grêmio', 'Santos', 'Internacional', 
'São Paulo', 'Corintians', 'Atlético-MG', 'Athletico-PR', 'Ceará', 'Vitória', 
'Cuiabá', 'Juventude')

print('-=' *30)
print(f'Os 5 primeiros colocados são {times[:5]}')
print('-=' *30)
print(f'Os últimos 4 colocados são {times[-4:]}')
print('-=' *30)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' *30)
print(f'Santos está na {times.index('Santos')+1}ª posição. ')



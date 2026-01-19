#Exercício Python 091: Crie um programa onde 4 jogadores
#joguem um dado e tenham resultados aleatórios. Guarde 
#esses resultados em um dicionário em Python. No final, 
#coloque esse dicionário em ordem, sabendo que o vencedor 
#tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter

apostas = dict()
ranking = list()

print()
print(f'{"APOSTAS SENDO FEITAS":^50}')
print()

for c in range(0,4):
    apostas[f'Jogador {c+1}'] = randint(1,10)

for k, v in apostas.items():
    print(f'{k} tirou {v} no dado. ')
    sleep(0.5)

ranking = sorted(apostas.items(), 
                 key=itemgetter(1), reverse=True)

print()
print('-='*25)
print(f'{"RANKING DOS JOGADORES":^50}')
print('-='*25)
print()

for i, v in enumerate(ranking):
    print(f'{i+1}⁰ lugar: {v[0]} com {v[1]}. ')
    sleep(0.5)



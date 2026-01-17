#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 
#6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

print('--'*30)
print('JOGA NA MEGA SENA'.center(60))
print('--'*30)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))

lista = []
todos = []

for _ in range(0,jogos):
    lista.clear()
    while len(lista) < 6:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    todos.append(lista[:])

print('-='*20)
for i, j in enumerate(todos):
    print(f'Jogo {i+1}:{j}')
print('Boa sorte!')
print('-='*20)
    
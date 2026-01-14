#Faça um programa que leia nome e peso de várias pessoas,
#guardando tudo em uma lista.
#No final mostre: a) Quantas pessoas foram cadastradas.
#b) Uma listagem com as pessoas mais pesadas.
#c) Uma listagem com as pessoas mais leves.

galera = []
maior = menor = 0

while True:
    nome = input('Nome: ')
    peso = int(input('Peso: '))
    galera.append([nome, peso])

    if len(galera) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    resp = input('Quer continuar [S/N]? ').upper().strip()[0]
    if resp == 'N':
        break

print(f'Total de pessoas cadastradas: {len(galera)}')

print('Pessoas mais pesadas:')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]} com {p[1]}kg')

print('Pessoas mais leves:')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]} com {p[1]}kg')

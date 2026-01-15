#Faça um programa que leia nome e peso de várias pessoas,
#guardando tudo em uma lista.
#No final mostre: a) Quantas pessoas foram cadastradas.
#b) Uma listagem com as pessoas mais pesadas.
#c) Uma listagem com as pessoas mais leves.

galera = []
maior = []
menor = []

while True:
    nome = input('Nome: ')
    peso = int(input('Peso: '))
    galera.append([nome, peso])

    if len(galera) == 1:
        maior = [nome, peso]
        menor = [nome, peso]
    else:
        if peso > maior[1]:
            maior = [nome, peso]
        if peso < menor[1]:
            menor = [nome, peso]

    resp = input('Quer continuar [S/N]? ').upper().strip()[0]
    if resp == 'N':
        break

print(f'Total de pessoas cadastradas: {len(galera)}')

print('Pessoas mais pesadas:')
print(maior)

print('Pessoas mais leves:')
print(menor)

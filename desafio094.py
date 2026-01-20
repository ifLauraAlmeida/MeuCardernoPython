#Exercício Python 094: Crie um programa que leia nome, sexo 
#e idade de várias pessoas, guardando os dados de cada pessoa 
#em um dicionário e todos os dicionários em uma lista. No final, 
#mostre: 
#    A) Quantas pessoas foram cadastradas 
#    B) A média de idade 
#    C) Uma lista com as mulheres 
#    D) Uma lista de pessoas com idade acima da média

pessoas = []
soma_idade = 0

while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: ')).title().strip()
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    
    pessoas.append(pessoa)
    soma_idade += pessoa['idade']
    
    resp = str(input('Quer continuar [S/N]? ')).upper().strip() [0]
    if 'S' not in resp:
        break
total = len(pessoas)
media = soma_idade / total

print(f'\nA) Total de pessoas: {total}.')
print(f'\nB) A média da idade: {media:.2f}')
print(f'\nC) Mulheres:', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('D) Pessoas acima da média: ')
for p in pessoas:
    if p['idade'] > media:
        print(f'{p['nome']} - {p['idade']} anos')



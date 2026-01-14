
#aula anterior - listas
# dados = list()
# dados.append('Pedro')
# dados append(250)
# print(dados[0])
# print(dados[1])


# pessoas = list()
# pessoas.append(dados[:]) #cópia de dados

# #ou

# pessoas = [['Pedro',25],['Maria', 19], ['João',32]]

# print(pessoas[0][0]) #Pedro
# print(pessoas[1][1]) #19
# print(pessoas[2][0]) #João
# print(pessoas[1]) # ['Maria', 19]


galera = list()
dado = list()
totmai = totmen = 0

for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    
print(galera)

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai+=1
    else:
        print(f'{p[0]} é menor de idade')
        totmen+=1
        
print(f'Temos {totmai} maiores e {totmen} menores de idade. ')

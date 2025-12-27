#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano 
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Na natação brasileira (CBDA), as categorias por idade são:
# Mirim: 8–9 anos
# Petiz: 10–11 anos
# Infantil: 12–13 anos
# Juvenil: 14–15 anos
# Júnior: 16–17 anos
# Sênior: 18+
# Idade considerada pelo ano de nascimento.

from datetime import datetime as dt

print('Bem vindo novo atleta!')

ano = int(input('Qual seu ano de nascimento?' ))
ano_atual = dt.now().year

idade = ano_atual - ano

if idade < 8:
    print('Sem categoria!')
elif 8 <= idade <= 9:
    print('Categoria: Mirim')
elif 10 <= idade <= 11:
    print('Categoria: Petiz')
elif 12 <= idade <= 13:
    print('Categoria: Infantil')
elif 14 <= idade <= 15:
    print('Categoria: Juvenil')
elif 16 <= idade <= 17:
    print('Categoria: Júnior')
else:
    print('Categoria: Sênior')
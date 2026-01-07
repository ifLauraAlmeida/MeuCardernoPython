# Exercício Python 075: Desenvolva um programa que leia quatro valores 
# pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

tupla = (int(input('Escolha um número: ')), int(input('Escolha outro número: ')), 
         int(input('Escolha outro número: ')), int(input('Escolha outro número: ')))


print(f'O número 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O número o número 3 aparece pela primeira vez na posição {tupla.index(3)+1}')
else:
    print('O número 3 não foi digitado')

print('Número pares digitados: ', end ='')

for n in tupla:
    if n % 2 == 0:
        print(n, end='')
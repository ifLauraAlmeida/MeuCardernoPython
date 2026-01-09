# Exercício Python 078: Faça um programa que leia 
# 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor 
# digitado e as suas respectivas posições na lista.

valores = []

for cont in range(0,5):
    valores.append(int(input('Digita um cacete dum valor ai: ')))

menor = min(valores)
maior = max(valores)

print(f'O menor valor da lista é {menor} na posição {valores.index(menor)}. ')
print(f'O maior valor da lista é {maior} na posição {valores.index(maior)}. ')
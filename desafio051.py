# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
# aqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print('-='*10)
print('10 TERMOS DE UMA PA')
print('-='*10)

prim_term = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = prim_term + (10 - 1) * razao

for c in range(prim_term,decimo + razao,razao):
    print(c, end=' -> ')
print('ACABOU')
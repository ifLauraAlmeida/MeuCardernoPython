# Exercício Python 060: Faça um programa que leia um número qualquer 
# e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Escolha um número: '))
fatorial = 1
c = n
print(f'{n}! = ', end='')

while c > 0:
    print(f'{c}', end='')
    fatorial *= c
    if c > 1:
        print(' x ', end='')
    c -= 1

print(f' = {fatorial}')
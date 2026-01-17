#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:  
# A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[],[],[]]
soma = 0

for l in range(0,3):
    for c in range(0,3):
        valor = int(input(f'Digite um valor para a linha {l} coluna {c}: '))
        matriz[l].append(valor)
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
            
print('-='*30)
print()
print(f'Esses são os valores da terceira coluna: ', end='')
print(f'{matriz[2]}')
print()
print('-='*30)
print()
print(f'A soma de todos os números pares é: {soma}')
print()
print('-='*30)
print()
print(f'O maior valor da segunda linha da matriz é: {max(matriz[1])}')
print()
print('-='*30)

#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:  
# A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[],[],[]]
soma = 0

for l in range(0,3):
    for c in range(0,3):
        valor = int(input(f'\033[42mDigite um valor\033[m para a linha\033[1;32m {l} \033[mcoluna \033[1;32m{c}\033[m: '))
        matriz[l].append(valor)
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

print()           
print('\033[44m-=\033[m'*30)
print()
print(f'Esses são os \033[4;34mvalores da terceira coluna\033[m: ', end='')
print(f'\033[44m{matriz[2]}\033[m')
print()
print('\033[44m-=\033[m'*30)
print()
print(f'A \033[4;34msoma\033[m de todos os \033[4;34mnúmeros pares\033[m é: \033[44m{soma}\033[m')
print()
print('\033[44m-=\033[m'*30)
print()
print(f'O \033[4;34mmaior valor da segunda linha da matriz\033[m é: \033[44m{max(matriz[1])}\033[m')
print()
print('\033[44m-=\033[m'*30)

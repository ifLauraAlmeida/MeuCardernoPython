# Exercício Python 52: Faça um programa que leia um número inteiro 
# e diga se ele é ou não um número primo. 

num = int(input('Digite um número: '))
cont = 0


for c in range (1,num+1):
    if num % c == 0:
        cont += 1
        print(f"\033[1;31m{c}\033[0m", end=' ')
    else:
        print(f"\033[0;34m{c}\033[0m", end=' ')

print(f"O número foi divisível {cont}")

if cont >= 3:
    print("E por isso ele não é primo!")
else:
    print("E por isso ele é primo!")

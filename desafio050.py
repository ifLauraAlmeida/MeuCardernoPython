# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
# aqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# num = []

# for c in range(6):
#     num.append(int(input('Digite um número: ')))

# soma = sum([n for n in num if n % 2 == 0])
# print(f'A soma dos números pares é: {soma}')


soma = 0
cont = 0 

for c in range(1,7):
    num = int(input(f"Digite o {c} valor: "))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f"Você informou {cont} números pares e a soma foi {soma}")
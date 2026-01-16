#Exercício Python 085: Crie um programa onde o usuário possa digitar 
#sete valores numéricos e cadastre-os em uma lista única que mantenha 
#separados os valores pares e ímpares. No final, mostre os valores pares 
#e ímpares em ordem crescente.

impares = []
pares = []

for i in range(0,7):
    n = int(input('Digite um valor: '))

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)   
pares.sort()
impares.sort()
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')
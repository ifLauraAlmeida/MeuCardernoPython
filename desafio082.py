#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores 
#ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista_principal = []
lista_impar = []
lista_par = []

while True:
    lista_principal.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if 'N' in resp:
        break
    
for valor in lista_principal:
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
        
print(f'A lista completa é: {lista_principal}')
print(f'A lista de pares é: {lista_par}')
print(f'A lista de impares é: {lista_impar}')

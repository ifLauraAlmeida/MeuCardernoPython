# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

resp = ''
lista = []

while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado!')
    else:
        lista.append(valor)
        print('Valor adicionado!')    
    
    resp = str(input(f'Quer continuar [S/N]? ')).upper().strip()[0]
    if 'S' not in resp:
        break

print('='*30)
print(f'Você digitou os valores: {sorted(lista)}')
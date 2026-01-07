# Exercício Python 076: Crie um programa que tenha uma tupla única 
# com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em 
# forma tabular.

listagem = ('Pizza', 29.90, 
            'Hamburguer', 18.87, 
            'Refrigerante', 8.50)

print('-'*30)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
       print(f'R${listagem[pos]:>7.2f}')
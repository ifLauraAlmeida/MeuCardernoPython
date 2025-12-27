# Exercício Python 44: Elabore um programa que calcule o valor a ser pago 
# por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço normal 

# – 3x ou mais no cartão: 20% de juros

valor_inicial = float(input('Qual o valor do produto? '))
print('''Escolha sua forma de pagamento:
[ 1 ] Á vista dinnheiro/cheque
[ 2 ] Á vista no cartão
[ 3 ] Até 2x no cartão
[ 4 ] 3x ou mais no cartão''')

forma_pag = int(input('Sua opção: '))

if forma_pag == 1:
    desconto = valor_inicial * 0.1
    valor = valor_inicial - desconto
    print(f"O valor final será R${valor:.2f}")
elif forma_pag == 2:
    desconto = valor_inicial *0.05
    valor = valor_inicial - desconto
    print(f"O valor final será R${valor:.2f}")
elif forma_pag == 3:
    print(f'''Não terá nenhum desconto ou acréscimo.
O valor fica em: R${valor_inicial:.2f}''')
elif forma_pag == 4:
    acrescimo = valor_inicial * 0.2
    valor = valor_inicial + acrescimo
    print(f"O valor final ficará em R${valor:.2f}")
else:
    print('Digite uma opção válida!')
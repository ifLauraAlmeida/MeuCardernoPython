# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: 
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

valorprodutomaisbarato = 0
caro = 0
while True:
    produto = str(input("Qual o nome do produto? "))
    preco = int(input("Qual o preço? "))
    if preco >= 1000:
        caro += 1
    
    barato = produto
    if  :

    tot += preco
    print("=="*25)
    print(f"""      O total gasto na compra foi: R${tot:.2f}.")
    O total de produtos que custam mais de R$1000 é: {caro}.
    """)
    print("=="*25)

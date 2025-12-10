# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = input("Digite um número de 0 a 9999: ")

# Inverter a string para processar de trás para frente (unidade primeiro)
num_invertido = num[::-1]

posicoes = ["unidade", "dezena", "centena", "milhar"]

i = 0
while i < len(num_invertido):
    print(f"{num_invertido[i]} - {posicoes[i]}")
    i += 1
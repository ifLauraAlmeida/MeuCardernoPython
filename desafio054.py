# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre 
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date 

nascimentos = []
for c in range(1, 8):
    nascimentos.append(int(input(f"Digite o ano de nascimento da pessoa {c}: ")))
    print(nascimentos)

ano_atual = date.today().year
maiores = menores = 0

for nasc in nascimentos:
    idade = ano_atual - nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"{maiores} pessoas são maiores de idade e {menores} são menores.")
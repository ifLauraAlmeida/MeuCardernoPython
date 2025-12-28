
# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.

pesos = []
for c in range(1,6):
    peso = float(input(f"Peso da {c} pessoa (kg): "))
    pesos.append(peso)

maior = max(pesos)
menor = min(pesos)

print(f'O maior peso foi {maior:.2f} kg')
print(f'O menor peso foi {menor:.2f} kg')
#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a 
#letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').lower().strip()

qtd_a = frase.count('a')
prm_a = frase.find('a') +1
ult_a = frase.rfind('a') +1


print(f"Nessa frase a letra 'A' aparece {qtd_a} vezes.")
print(f"Nessa frase a primeira letra 'A' aparece na posição {prm_a}")
print(f"Nessa frase a última letra 'A' aparece na posição {ult_a}")


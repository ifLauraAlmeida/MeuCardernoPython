
#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
#desconsiderando os espaços. Exemplos de palíndromos:
#APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Diga uma frase: ')).lower().strip()
sem_espaco = ''.join(frase.split())
print(sem_espaco)

if sem_espaco == sem_espaco[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')
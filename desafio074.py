# Exercício Python 074: Crie um programa que vai gerar cinco números 
# aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique 
# o menor e o maior valor que estão na tupla.
from random import randint

numero = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'A listagem de números foi: {numero}')
print(f'O maior número da lista foi: {max(numero)}')
print(f'O menor número da lista foi: {min(numero)}')
      

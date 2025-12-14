# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input('Qual seu nome completo? ').lower().strip()
print('Seu nome tem SILVA? ')

if "silva" in nome:
    print(True)
else:
    print(False)

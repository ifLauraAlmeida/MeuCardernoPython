#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input('Qual seu nome completo?'))
#Nome maiúsculo
print('Seu nome com todas as letras maiúsculas fica: ', nome.upper())
#Nome minusculo
print('Seu nome com todas as letras minusculas fica: ', nome.lower())
#Quantas letras tem o nome todo
nometd = nome.strip()
print(f'Seu nome tem {len(nometd) - nome.count(' ')} letras.')
#Quantas letras tem o primeiro nome
primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras.')

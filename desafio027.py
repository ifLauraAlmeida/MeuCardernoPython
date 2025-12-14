#Faça um programa que leia o nome completo de uma pessoa, mostrando 
# em seguida o primeiro e o último nome separadamente. 

nome_completo = input('Digite seu nome completo: ').lower().strip()

nome_dividido = nome_completo.split()
primeiro_nome = nome_dividido[0]
ultimo_nome = nome_dividido[-1]

print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu último nome é {ultimo_nome}')
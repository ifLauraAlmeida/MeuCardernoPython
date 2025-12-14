#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Qual cidade você nasceu? ').lower().strip()

print(cidade) #ver se o lower e o strip funcionaram

print(cidade[:5] == 'santo')

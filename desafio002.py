nome=input('Qual é o seu nome?')
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}

print('Olá, '+nome,'! Prazer em te conhecer!')   
print(f'Olá, {cores["azul"]}{nome}{cores["limpa"]} ! Prazer em te conhecer!')
print('Olá, {} l ! Prazer em te conhecer!'.format(nome) )
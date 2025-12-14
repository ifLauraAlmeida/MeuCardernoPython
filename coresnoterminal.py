print('\033[1;31;43mOlá mundo!\033[m')
#mostre cores diferentes no mesmo texto
nome = 'Ana'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
#outra forma de fazer
nome = 'Ana'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}
print(f'Olá! Muito prazer em te conhecer, {cores["azul"]}{nome}{cores["limpa"]}!!!')
# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras 
# (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais 
# são as suas vogais.

palavra = 'python', 'mercado', 'jogo', 'sabonete', 'buriti'

for p in palavra:
    print(f'\n Na palavra \033[45m {p.upper()} \033[m temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[44m {letra} \033[m', end='')
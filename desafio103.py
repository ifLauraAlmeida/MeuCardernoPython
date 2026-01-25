# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que
# vai funcionar de forma semelhante ‘a função input() do Python, só que 
# fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ‘)

def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')

#Programa principal
n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
#Exercício Python 113: Reescreva a função leiaInt()
#que fizemos no desafio 103, incluindo agora a 
#possibilidade da digitação de um número de tipo 
#inválido. Aproveite e crie também uma função leiaFloat() 
#com a mesma funcionalidade.

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
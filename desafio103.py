# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que
# vai funcionar de forma semelhante ‘a função input() do Python, só que 
# fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ‘)

def leia_int(msg):
    while True:
        entrada = input(msg).strip()
        
        valido = True
        for caractere in entrada:
            if caractere not in '-0123456789':
                valido = False
                break
        
        if not valido:
            print('ERRO! Digite um número inteiro válido.')
            continue
        
        n = int(entrada)
        return n

#Programa principal
n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
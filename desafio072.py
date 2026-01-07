#Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
#de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = 'zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
num = int(input('Escolha um número para escrever por extenso: '))

while True:
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f"Você digitou o número {extenso[num]}")
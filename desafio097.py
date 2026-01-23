#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), 
#que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho 
#adaptável. Ex: escreva(‘Olá, Mundo!’) Saída: Olá, Mundo!

def escreva(frase):
    tam = len(frase)
    print('*' * (tam + 4))
    print(f'  {frase}')
    print('*' * (tam + 4))
frase = str(input('Digite uma frase: '))
escreva(frase)
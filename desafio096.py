#Exercício Python 096: Faça um programa que tenha 
#uma função chamada área(), que receba as dimensões 
#de um terreno retangular (largura e comprimento)
#e mostre a área do terreno.
a=0

def area(l,c):
    a = ((l**2)+(c**2))
    print(f'A área de um terreno de dimensões:\n{l} m² Largura\n{c} m² Comprimento\nÉ igual a: {a} m².')

l=int(input('Qual a largura do terreno? '))
c=int(input('Qual o comprimento do terreno? '))
area(l,c)
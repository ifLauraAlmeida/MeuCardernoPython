#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar 
# que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes 

a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))

if a < b + c and b < a + c and c < a + b:
    print('Forma triângulo.')
    if a == b == c:
        print('EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Não forma triângulo.')

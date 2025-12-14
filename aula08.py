"""
Bebidas = Coca, Suco, Agua
Doce = Chocolate, Bala, Pirulito

import bebida (vai importar coca, suco e agua)
from doce import * (vai importar chocolate, bala e pirulito)
from doce import chocolate (vai importar somente chocolate)

Dessa forma funciona para módulos, funcionam como pacotes
com funcionalidades, como doce e bebida.
Doce e bebida são módulos. 
Suas funcionalidades são como se fossem suco, chocolate...

Biblioteca Math (import math)
ceil (arrendonda para cima)
floor (arrendonda para baixo)
sqrt (raiz quadrada)
pow (potência)
fabs (valor absoluto) 
factorial (fatorial)
trunc (corta as casas decimais)

import math 
from math import sqrt, floor

import math

num = int(input("Digite um número: "))
raiz = math.sqrt(num)

print('A raiz quadrade de {} é igual a {}'.format(num, raiz))

print('A raiz quadrade de {} é igual a {}'.format(num, math.ceil(raiz)))

print('A raiz quadrade de {} é igual a {}'.format(num, math.floor(raiz)))

Biblioteca Random (import random)
random() (número aleatório entre 0 e 1)
randint (número inteiro aleatório entre os valores estabelecidos)
uniform (número real aleatório entre os valores estabelecidos)

import random 
num = random.random()
print(num)

num = random.randint(1, 10)
print(num)

num = random.uniform(1, 10)
print(num)


Pra saber quais bibliotecas já estão instaladas:
pip list

"""
import math

num = (input("Digite um número: "))
raiz = math.sqrt(num)

print('O número inteiro de {} é igual a {}'.format(num, raiz))

print('O número inteiro de {} é igual a {}'.format(num, ceil(raiz)))

print('O número inteiro de {} é igual a {}'.format(num, floor(raiz)))

from math import ceil, floor, trunc
"""import math as mt"""

entrada = input("Digite um número real: ")
entrada = entrada.replace(",", ".")
num = float(entrada)

print("O número digitado foi {} e sua porção inteira é {}".format(num, math.trunc(num)))
print("O número digitado foi {} e sua porção inteira é {}".format(num, math.floor(num)))
print("O número digitado foi {} e sua equivalência para cima é {}".format(num, math.ceil(num)))

""" print("O número digitado foi {} e sua porção inteira é {}".format(num, math.trunc(num)))
     para não usar "from math import trunc" 
    print('O número digitado foi {} e sua porção inteira é {}'.format(num, int(num)))
    para não importar nenhuma biblioteca
"""



def multi(x):
    for y in range(0,11):
        res = x * y
        print(f"{x} x {y} = {res}")
def soma(y,x):
    res = y + x
    print(f"{y} + {x} = {res}")
    
def sub(y,x):
    res = y - x
    print(f"{y} - {x} = {res}")

print(''' Qual operação você deseja fazer?
      [ 1 ] Soma
      [ 2 ] Subtração
      [ 3 ] Multiplicação''')
escolha = int(input("Escolho a "))

if escolha == 1:
    y = int(input("Quero somar: "))
    x = int(input("Com: "))
    soma(x,y)
    
if escolha == 2:
    y = int(input("Quero diminuir: "))
    x = int(input("Com: "))


if escolha == 3:
    x = int(input("Você quer a tabuada de qual número? "))
    multi(x)

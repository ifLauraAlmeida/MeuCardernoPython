##FUNÇÕES
#print() len() input() int() são funções!

#def titulo(txt):
    #print('-'*30)
    #print(txt)
    #print('-'*30)
    
#Programa Principal
#titulo('   Curso em Vídeo   ')
#titulo('   Aprenda Python   ')
#titulo('  Gustavo Guanabara  ')


a = 4
b = 5
s = a + b
print(s)
a = 8 
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)

#mesma coisa que
from time import sleep
from random import randint

def soma(a, b):
    while True:
        print(f'Os números escolhidos foram {a} e {b}.')    
        sleep(1)
        print(f'A soma deles fica: {a + b}. ')
        sleep(1)
        resp = int(input('''
        Responda [0] - Para continuar
        Responda [1] - Para parar
        '''))
        sleep(1)
        if resp == 0:
            print("Continuando...")
        elif resp == 1:
            print("Parando...")
        else:
            print("Opção inválida")

soma(randint(1,10), randint(1,10))

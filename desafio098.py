#Exercício Python 098: Faça um programa que tenha 
#uma função chamada contador(), que receba três 
#parâmetros: início, fim e passo. Seu programa 
#tem que realizar três contagens através da 
#função criada:
    #a) de 1 até 10, de 1 em 1  
    #b) de 10 até 0, de 2 em 2  
    #c) uma contagem personalizada
from time import sleep

def contador(i,f,p):
    print(f'Contagem de {i} até o {f} de {p} em {p}')
    
    if i<f:
        cont=i
        while cont <= f:
            print(f'{cont} ', end='')
            cont+=p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont-=p
        print('FIM!')
def divisoria():
    print('-='*30)
    
divisoria()
contador(10,1,1)
divisoria()
sleep(1)
contador(1,10,1)
divisoria()
sleep(1)

print('Agora é sua vez de personalizar a categoria')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
divisoria()
contador(i,f,p)
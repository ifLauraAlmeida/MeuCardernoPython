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


#a = 4
#b = 5
#s = a + b
#print(s)
#a = 8 
#b = 9
#s = a + b
##print(s)
#a = 2
#b = 1
#s = a + b
#print(s)

#mesma coisa que
#from time import sleep
#from random import randint

#def soma(a, b):
    #while True:
        #print(f'Os números escolhidos foram {a} e {b}.')    
        #sleep(1)
        #print(f'A soma deles fica: {a + b}. ')
        #sleep(1)
        #resp = int(input('''
        #Responda [0] - Para continuar
        #Responda [1] - Para parar
        #'''))
        #sleep(1)
        #if resp == 0:
            #print("Continuando...")
        #elif resp == 1:
            #print("Parando...")
        #else:
            #print("Opção inválida")

#soma(randint(1,10), randint(1,10))

#EMPACOTAMENTO
#def contador(*num):
    #print(num)
    #tam = len(num)
    #print(f`Recebi os valores {num} e sáo ao todo {tam} numeros`.)
#contador(2,1,7)
#contador(8,0)
#contador(4,4,6,2)
#def dobra(lst):
    #pos = 0
    #while pos < len(lst):
        #lst[pos]*=2
        #pos+=1
#valores = [6,3,9,1,0,2]
#dobra(valores)
#print(valores)

#def soma(*valores): # * significa que “posso receber vários valores, não sei quantos”. 
    #s = 0           # Tudo o que é passado vira tupla.
    #for num in valores:
        #s+=num
    #print(f'Somando os valores {valores} temos {s}')
#soma(5,2)
#soma(2,9,4)
#Faca um programa que mostra na tela uma contagem regressiva para o estouro de fogos de artifício.
#Indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time as tm

inicio = tm.time() #indicar o inicio da execução do código

for i in range (10,0,-1):
    print(i)
    tm.sleep(1) #esperar 1 segundo pra voltar ao laço de repetição

print('UHUL!🎆🧨')

fim = tm.time() #indicar o final da execução
print(f'Tempo total: {fim - inicio:.2f} segundos') #printar o tempo 


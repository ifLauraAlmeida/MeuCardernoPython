# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                 
# A) Quantos números foram digitados.                
# B) A lista de valores, ordenada de forma decrescente.      
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = []

while True:
    
    valores.append(int(input('Digita um cacete dum valor ai: ')))
    
    resp = str(input('Deseja continuar [S/N]?')).upper().strip()[0]
    
    if 'S' not in resp:
        break
    
print(f'Você digitou {len(valores)} elementos. ')
print(f'Os valores em ordem decrescente são: {sorted(valores, reverse=True)}')  # reverse=True para inverter a ordem para decrescente
#print(f'Os valores em ordem decrescente são: {valores.sort(rever=True)}')
# sort() → modifica a lista
# sorted() → retorna uma nova lista

if 5 in valores: #se colocar o 5 em aspas ele entende que é string
    print('O valor 5 faz parte da lista! ')
else:
    print('O valor 5 não faz parte da lista!' )


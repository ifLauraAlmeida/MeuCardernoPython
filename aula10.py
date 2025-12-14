##Estruturas condicionais

tempo = int(input('quantos anos tem seu carro?'))
if  tempo <=3:
    print('carro novo')
else:
    print('carro velho')    
print('--FIM--')

#forma simplificada

tempo = int(input('quantos anos tem seu carro?'))
print('carro novo' if tempo <=3 else 'carro velho')
print('--FIM--')

#Desafio
#Faça um programa que leia duas notas de um aluno, calcule e mostre a sua média.
#Mostre uma mensagem no final, de acordo com a média atingida
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('PARABÉNS! Você foi aprovado!')
else:
    print('ESTUDE MAIS! Você foi reprovado!')
print('--FIM--')

#forma simplificada

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
print('PARABÉNS! Você foi aprovado!' if m >= 6.0 else 'ESTUDE MAIS! Você foi reprovado!')
print('--FIM--')
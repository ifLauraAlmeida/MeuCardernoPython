# #Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura 
# de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
# de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso

# – Entre 18,5 e 25: Peso Ideal

# – 25 até 30: Sobrepeso

# – 30 até 40: Obesidade


print('Olá, vamos calcular seu IMC!')
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

imc = peso / altura

if imc <= 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Peso ideal')
elif 25 <= imc <= 30:
    print('Sobrepeso')
else:
    print('Obesidade')
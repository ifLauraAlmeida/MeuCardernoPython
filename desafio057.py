# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''
while sexo not in ['m','f']: #enquanto SEXO não é registrado com m ou f, ele repete o laço.
    sexo = str(input('Qual seu gênero? [M/F] ' )).strip().lower()[0] #tira os espaços, transforma em minusculo
    if sexo not in 'mf':                                        #e retira apenas a primeira letra digitada
        print("Dados inválidos, informe seu sexo corretamente.")
    else:
        print("Sexo registrado!")
print("Fim")


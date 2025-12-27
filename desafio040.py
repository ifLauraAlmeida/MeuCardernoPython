#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:

nota1 = float(input('Qual sua nota em matemática? '))
nota2 = float(input('Qual sua nota em português? '))

media = (nota1 + nota2) / 2

if media >= 5:
    print(f"Sua nota tem uma média de {media} e ela é suficiente para passar de ano!")
else:
    print(f"Sua nota tem uma média de {media} e ela não é suficiente para passar de ano!")
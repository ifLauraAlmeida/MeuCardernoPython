#Exercício Python 090: Faça um programa que leia nome e média de um aluno, 
#guardando também a situação em um dicionário. No final, mostre o conteúdo 
#da estrutura na tela.

cadastro_aluno = dict()
turma = list()

cadastro_aluno['nome_aluno'] = str(input('Qual o nome dele? ')).title()
cadastro_aluno['media'] = float(input('Media do aluno? '))

if cadastro_aluno['media'] <= 5:
    cadastro_aluno['situacao'] = 'Recuperação'
else:
    cadastro_aluno['situacao'] = 'Aprovado'

turma.append(cadastro_aluno.copy())

for a in turma:
    for k, v in a.items():
        print(f'-{k} é igual {v:.2f}. ')
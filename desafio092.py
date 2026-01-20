#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira 
#de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for 
#diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime

cadastro_func = dict()

cadastro_func['nome'] = str(input('Primeiro nome: ')).title()
cadastro_func['ano_nascimento'] = int(input('Ano de nascimento: '))
cadastro_func['carteira_trabalho'] = int(input('CTPS: '))
cadastro_func['idade'] = datetime.now().year - cadastro_func['ano_nascimento']

if cadastro_func['carteira_trabalho'] != 0:
    cadastro_func['ano_contratacao'] = int(input('Ano de contratação: '))
    cadastro_func['salario'] = int(input('Salário: '))
    cadastro_func['aposentadoria'] = cadastro_func['idade'] + ((cadastro_func['ano_contratacao'] + 35) - datetime.now().year)
print()
print(f'-='*30)
print()
for k, v in cadastro_func.items():
    print(f"{k}: {v}")

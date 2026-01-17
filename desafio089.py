#Exercício Python 089: Crie um programa que leia nome e duas notas de vários 
#alunos e guarde tudo em uma lista composta. No final, mostre um boletim 
#contendo a média de cada um e permita que o usuário possa mostrar as notas 
#de cada aluno individualmente.

dados_turma = []

AZUL = '\033[1;34m'
AMARELO = '\033[1;33m'
FUNDO_AMARELO = '\033[1;44m'
NEGRITO = '\033[1m'
RESET = '\033[m'

# ===== Cadastro =====
print(f'{FUNDO_AMARELO}{NEGRITO} SISTEMA DE BOLETIM ESCOLAR {RESET}')
print()

while True:
    nome = input(f'{AZUL}Nome do aluno:{RESET} ').strip().title()
    nota1 = float(input(f'{AMARELO}Nota de Português:{RESET} '))
    nota2 = float(input(f'{AMARELO}Nota de Matemática:{RESET} '))
    media = (nota1 + nota2) / 2

    dados_turma.append([nome, nota1, nota2, media])

    resp = input(f'{AZUL}Deseja continuar [S/N]? {RESET}').upper().strip()[0]
    if resp != 'S':
        break

# ===== Boletim =====
print()
print(f'{AZUL}-=' * 20 + RESET)
print(f'{NEGRITO}{AMARELO}{"No.":<4}{"NOME":<15}{"MÉDIA":>6}{RESET}')
print(f'{AZUL}-' * 30 + RESET)

for i, aluno in enumerate(dados_turma):
    print(f'{i:<4}{aluno[0]:<15}{AMARELO}{aluno[3]:>6.1f}{RESET}')

print(f'{AZUL}-' * 30 + RESET)

# ===== Consulta individual =====
while True:
    opcao = int(input(f'{NEGRITO}Ver notas de qual aluno? '
                      f'{AMARELO}(No ou 999 para sair): {RESET}'))

    if opcao == 999:
        print(f'{AZUL}Encerrando consulta.{RESET}')
        break

    if opcao < 0 or opcao >= len(dados_turma):
        print(f'\033[1;31mAluno inexistente.{RESET}')
    else:
        print(f'{NEGRITO}Notas de {dados_turma[opcao][0]}:{RESET} '
              f'{AMARELO}{dados_turma[opcao][1]}{RESET} e '
              f'{AMARELO}{dados_turma[opcao][2]}{RESET}')



    
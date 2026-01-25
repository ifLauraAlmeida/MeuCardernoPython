#Exercício Python 105: Faça um programa que tenha 
#uma função notas() que pode receber 
#várias notas de alunos e vai retornar um 
#dicionário com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota 
#-A média da turma 
#– A situação (opcional)

def notas(*n, sit=False):
    """
    -> Analisa notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos
    :param sit: (opcional) indica se deve mostrar a situação
    :return: dicionário com os dados da turma
    """
    resp = {}
    resp['total'] = len(n)
    resp['maior'] = max(n)
    resp['menor'] = min(n)
    resp['media'] = sum(n) / len(n)

    if sit:
        if resp['media'] >= 7:
            resp['situacao'] = 'BOA'
        elif resp['media'] >= 5:
            resp['situacao'] = 'RAZOÁVEL'
        else:
            resp['situacao'] = 'RUIM'

    return resp


# Programa principal
aluno = notas(5.5, 2.5, 1.5, sit=True)
print(aluno)

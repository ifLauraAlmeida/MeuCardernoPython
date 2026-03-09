from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        #OPÇÃO DE LISTAR CONTEÚDO DE UM ARQUIVO
        lerarquivo(arq)
    elif resposta == 2:
        #OPÇÃO DE CADASTRAR UMA NOVA PESSOA
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
        
    elif resposta == 3:
        cabecalho('Saindo do sistema... até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida.')
    sleep(2)


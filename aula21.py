#FUNÇÕES PARTE 2

#Interactive Help:
#É uma função interna "help()", um método.
#Como usar:
#help()
#Ele te ajuda a entender melhor outras funções do python
#ou help(print)
#ou print(input.__doc__)

#DOCSTRINGS
#É uma string de documentação.
#def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: incio da contagem
    :param f: fim da contagem
    :paramentro passo da contagem
    :return: sem retorno
    
    Função criada por Laura
    """
    #c=i
    #while c<=f:
        #print(f'{c}', end='..')
        #c+=p
    #print(f'FIM!')

#contador(1,100,1)  #I=1  F=100  P=1 

#help(contador)

#PARAMETROS OPCIONAIS
#SEM
#def somar(a,b,c):
#   s=a+b+c
#   print(f'A soma vale {s}')
#
#somar(3,2,5)
#COM
#def somar(a=0,b=0,c=0):
#   s=a+b+c
#   print(f'A soma vale {s}')
#
#somar(3,2)

# ================================
# ESCOPO DE VARIÁVEIS EM PYTHON
# (Curso em Vídeo - Gustavo Guanabara)
# ================================

# Escopo define ONDE a variável funciona no programa.

# ----------------
# ESCOPO GLOBAL
# ----------------
# Variáveis criadas fora de funções.
# Podem ser usadas em qualquer parte do código.
# Funções conseguem LER variáveis globais.

#x = 10  # variável global

# ----------------
# ESCOPO LOCAL
# ----------------
# Variáveis criadas dentro de funções.
# Só existem dentro da função onde foram criadas.
# Fora da função, elas NÃO existem.

#def exemplo():
    #y = 5  # variável local

# ----------------
# VARIÁVEL GLOBAL DENTRO DA FUNÇÃO
# ----------------
# Se tentar MODIFICAR uma variável global dentro
# da função, o Python entende como variável local.

# Para modificar uma global dentro da função,
# é necessário usar a palavra-chave global.

# Ex:
# global x

# ----------------
# BOA PRÁTICA (DICA DO GUANABARA)
# ----------------
# Evite usar 'global'.
# O melhor é retornar valores com return.

# Variável local manda dentro da função.
# Variável global manda fora da função.


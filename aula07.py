nome=input('Qual é o seu nome? ')
print('Prazer em te conhecer, {:=^20}!'.format(nome))
# :=²0 = alinha o texto ao centro, com 20 caracteres de largura, preenchendo com '='
# < alinha à esquerda
# > alinha à direita
# ^ alinha ao centro
# :20 define a largura mínima do campo como 20 caracteres
# :0>20, por exemplo, alinha à direita e preenche com zeros à esquerda
# :0<20 alinha à esquerda e preenche com zeros à direita
# :^20 alinha ao centro e preenche com espaços à esquerda e à direita
# :^=20 alinha ao centro e preenche com '=' à esquerda e à direita
# :^*20 alinha ao centro e preenche com '*' à esquerda e à direita
# :^!20 alinha ao centro e preenche com '!' à esquerda e à direita
# :^~20 alinha ao centro e preenche com '~' à esquerda e à direita
# :^-20 alinha ao centro e preenche com '-' à esquerda e à direita
# :^+20 alinha ao centro e preenche com '+' à esquerda e    à direita
# :^_20 alinha ao centro e preenche com '_' à esquerda e à direita
# :^ 20 alinha ao centro e preenche com espaços à esquerda e à direita 
n1=int(input('Um valor:'))
n2=int(input('Outro valor:'))
print('A soma vale {}'.format(n1+n2))
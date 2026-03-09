#Exercício Python 114: Crie um código em Python 
# que teste se o site está acessível pelo 
# computador usado.

import urllib.request

try:
    site = urllib.request.urlopen('https://subhue.org')
except urllib.error.URLError:
    print('O site do Google não está disponível no momento.')
else:
    print('Consegui acessar o google com sucesso.')
    print(site.read())
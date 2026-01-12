# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr = input('Digite a expressão: ')
pilha = []

for c in expr:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if not pilha:
            pilha.append(')')  # erro
            break
        pilha.pop()

if not pilha:
    print('Parênteses estão corretos')
else:
    print('Parênteses estão incorretos')

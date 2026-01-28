#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as 
# funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

#Exercício Python 108: Adapte o código do desafio #107, criando uma 
# função adicional chamada moeda() que 
#consiga mostrar os números como um valor monetário formatado.

#Exercício Python 109: Modifique as funções que form criadas no
# desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não 
# formatado pela função moeda(), desenvolvida no desafio 108.
import moeda

num = float(input('Digite o preço: '))
print(f'O dobro de R${num:.2f} é igual á {moeda.moeda(moeda.dobro(num))}.')
print(f'A metade de R${num:.2f} é igual á {moeda.moeda(moeda.metade(num))}.')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(num))}.')
print(f'Diminuindo 10%, temos {moeda.moeda(moeda.diminuir(num))}.')
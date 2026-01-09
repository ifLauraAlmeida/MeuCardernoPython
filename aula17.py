# #LISTAS
# #As tuplas são boas pra guardar elementos, lanche = ('hamburguer', 'suco', 'pizza', 'pudim'), o python entende esses index como começando
# #por 0 e indo até 3, pois trata-se de 4 alimentos. print(lanche[2]) amostraria a pizza. lanche[3]='picole', mas as tuplas são imutáveis, então
# #isto é impossível.
# #Para isso, seria necessário usar uma lista. Tuplas () e Listas []. As listas também tem o index indo de 0 a 4, e nesse caso, o lanche[3]='pudim'
# #funcionaria pois as listas SÃO MUTÁVEIS.
# lanche = ['hamburguer','suco','pizza','pudim']
# lanche[3]='picolé'
# print(lanche[3])
# #Como as listas são mutáveis, você poderia acrescentar nessa lista, coisas do lado do pudim, porém não é tão simples. Para adiiconar coisas na
# #lista se usa o comando .APPEND().
# lanche.append('biscoito') #método append
# print(lanche[4])
# #Este comando ele irá SEMPRE adicionar ao FINAL da lista.
# print(lanche)
# #Você pode adicionar um item no incio da lista.
# lanche.insert(0,'cachorro quente')
# print(lanche[0])
# print(lanche)

# #Você também pode remover itens da lista.
# #del lanche[0] #comando del
# #ou
# #lanche.pop(0) #normalmente ele é usado para deletar o ULTIMO item de uma lista. # método pop
# #Se você não indicar o índice pro pop, ele deleta o ÚLTIMO elemento da lista.
# #ou
# #lanche.remove('pizza') #no remove você não usa o indice, e sim o nome na lista. #método remove
# print(lanche)
# #Todos estes, eliminam o elemento que ocupava o índice e refaz os índices, se ia do 0 até o 10, fica indo do 0 até o 9, certinho.
# #Se ocorrer de você tentar remover algum item que já não está mais, o programa apresenta um erro, porém existe como você VERIFICAR
# #se aquele elemento se encontra ainda na lista.
# if 'cachorro quente' in lanche:
#     lanche.remove('cachorro quente')
#     print(f'Removemos o cachorro quente da lista verificando antes com o in: \n {lanche}.')
# #Você também pode criar listas através de ranges:
# valores = list(range(4,11))
# #Você pode organizar em ordem valores desorganizados com o .sort()
# valores=[8,2,5,4,9,3,0]
# valores.sort()
# print(valores)
# Para organizá-los ao contrario.
# valores.sort(reverse=True)
# print(valores)
# #Para saber o tamanho da lista:
# print(len(valores))

########LAÇOS COM LISTAS

valores = []

for cont in range(0,5):
    valores.append(int(input('Digita um cacete dum valor ai: '))) 

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}! ')
print('Cheguei ao final da lista.')

#DISCLAIMER SOBRE IGUALAR A MESMA LISTA A UMA OUTRA:
#a = [3,4]
#b = a
#b[2] = 2
# AS DUAS AINDA ASSIM SÃO IGUAIS.
# você não copia uma lista, você liga elas.
#pra copiar, você precisa "fatiar"
#b = a[:] !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
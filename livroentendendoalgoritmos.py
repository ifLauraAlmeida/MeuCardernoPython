# def pesquisa_binaria(lista, item):
#     baixo = 0
#     alto = len(lista) - 1

#     while baixo <= alto:
#         meio = (baixo + alto) // 2  # divisão inteira
#         chute = lista[meio]

#         if chute == item:
#             return meio #
#         elif chute > item:
#             alto = meio - 1
#         else:
#             baixo = meio + 1

#     return None  # fora do while


# minha_lista = [1, 3, 5, 7, 9]

# print(pesquisa_binaria(minha_lista, 3))   # 1
# print(pesquisa_binaria(minha_lista, -1))  # None

def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoporSelecao([5, 3, 6, 2, 10]))
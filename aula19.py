#Dicionários

pessoas = {'nome':'Laura',
           'sexo':'feminino',
           'idade':'25'}
#print(pessoas) #output: {'nome': 'Laura', 'sexo': 'feminino', 'idade': '25'}
#print(pessoas[0]) #output: erro
#print(pessoas['nome']) #output: Laura
#print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.') #output: A Laura tem 25 anos.
#print(pessoas.keys()) #output: dict_keys(['nome', 'sexo', 'idade'])
#print(pessoas.values()) #output: dict_values(['Laura', 'feminino', '25'])
#print(pessoas.items()) #output: dict_items([('nome', 'Laura'), ('sexo', 'feminino'), ('idade', '25')])
#for k,v in pessoas.items():
#    print(f'{k} = {v}')    #output: nome = Laura
                                   #sexo = feminino
                                   #idade = 25
#del pessoas ['sexo']   # apaga o item sexo do dicionário
#pessoas['nome'] = 'Leandro'   # modifica o nome dentro do dicionário
#pessoas['peso'] = 98.5 # adiciona o item peso com um valor atrelado a ele


#brasil = []

#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

#brasil.append(estado1)
#brasil.append(estado2)

#print(brasil) #vira uma lista com dicionários
#print(brasil[0]) #mostra o primeiro dicionário adicionado
#print(brasil[0]['uf']) #output: Rio de Janeiro

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: ')).title()
    estado['sigla'] = str(input('Sigla do Estado: ')).upper()[:2]
    brasil.append(estado.copy()) # substitui o que seria o brasil.append(estado[:]) o FATIAMENTO
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
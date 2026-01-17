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
for k,v in pessoas.items():
    print(f'{k} = {v}')
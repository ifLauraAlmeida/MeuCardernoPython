preco = float(input('Digite o preço do produto: R$'))
desconto = preco * 0.05
precofinal = preco - desconto
print('O preço do produto com 5% de desconto é R$ {:.2f}'.format(precofinal)) 

precofinal = preco * 5 / 100
print('O preço do produto com 5% de desconto é R$ {:.2f}'.format(preco - precofinal))

precofinal = preco - (preco * 5 / 100)
print('O preço do produto com 5% de desconto é R$ {:.2f}'.format(precofinal))

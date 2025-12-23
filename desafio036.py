#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor da casa?'))
salario =  float(input('Qual seu salário?'))
anos = float(input('Em quantos anos pagará?'))

por_salario = salario * 0.3
mes = anos * 12
parcela_casa = valor_casa / mes

if parcela_casa <= por_salario:
    print('Você poderá pegar o empréstimo para a casa!')
else:
    print('Não vai rolar, arrume um emprego melhor.')
# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. 

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

opcao = 0

while opcao != 5:
    print('''Você pode...
       [ 1 ] Somar
       [ 2 ] Multiplicar
       [ 3 ] Maior
       [ 4 ] Novos números
       [ 5 ] Sair do programa ''')
    opcao = int(input('Selecione uma opção: '))
    if opcao == 1:
        soma = num1 + num2
        print(f"A soma do primeiro com o segundo número é: {soma}")
    elif opcao == 2:
        mult = num1 * num2
        print(f"A multiplicação do primeiro com o segundo número é: {mult}")
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f"Entre {num1} e {num2} o maior valor é {maior}")
    elif opcao == 4:
        print("Informe os números novamente: ")
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente!")
    print("-="*10)
print('Fim do programa, volte sempre!')



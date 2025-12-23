#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou 
#do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('Me diga sua idade: '))

if idade < 18:
    print('Você deverá se alistar ainda.')
    falta = 18 - idade
    print(f"Faltam {falta} anos para você ter que se alistar.")
elif idade > 18:
    print('Você passou da hora de se alistar!')
    atrasado = idade - 18
    print(f"Você está a {atrasado} anos atrasado para se alistar.")
else:
    print('Você deverá se alistar agora!')
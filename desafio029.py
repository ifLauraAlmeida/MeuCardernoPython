#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por 
#cada Km acima do limite.

vel = int(input('Em qual velocidade você esta?'))

if vel >= 80:
	limite = vel - 80
	multa = limite * 7
	print(f"Você atintiu o limite permitido da via. Deverá pagar uma multa de R${multa:.2f}.")

print('Dirija com segurança, tenha um bom dia!')
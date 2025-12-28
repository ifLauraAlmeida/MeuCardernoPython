# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

import random as rd

numpc = rd.randint(0,10)

numuser = int(input('Tente acertar o número que o computador pensou: '))

tentativas = 1
while numuser != numpc:
    tentativas += 1
    numuser = int(input('VOCÊ ERROU, tente novamente: '))

print(f"Caramba, você acertou, o número era de fato {numpc}")
print(f"Você precisou de {tentativas} para solucionar!")
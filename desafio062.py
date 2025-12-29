# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos. 

print('-='*10)
print('GERADOR DE PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
total = 0
mais = 10

while mais != 0:
    contador = 0
    while contador < mais:
        print(f"{termo} -> ", end='')
        termo += razao
        contador += 1
        total += 1
    print('PAUSA')
    print()  # pular linha antes de perguntar
    mais = int(input('Você deseja ver mais alguns termos? Quantos? (0 para sair) '))

print(f'FIM. Progressão finalizada com {total} termos mostrados.')

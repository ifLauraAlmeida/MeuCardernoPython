# Manipulando textos em Python
# No python, toda cadeia de texto como "curso em video" ou 'curso em video', pode ser chamada de string.

frase = 'Curso em Video Python'
# Aqui você atribui a uma variável, esta string.
# O python armazena cada caractere da string em uma posição da memória do computador, como caixinhas, inclusindo o espaço.
# Sendo assim, cada caractere tem um índice, que começa em 0 e nesse caso vai até o 20. Sendo 21 caracteres no total.
# FATIAMENTO DE STRINGS
print(frase[9])      # Mostra o caractere que está na posição 9
print(frase[0:6])   # Mostra do caractere 0 até o 6 (atenção pois o ultimo caractere não entra, entao o 6 não entra)
print(frase[9:21:2]) # Ele mostra do 9 ao 21 porém pulando um a cada leitura
print(frase[:6])   # Mostra do começo até o 6 (o 6 não entra)
print(frase[9:])   # Mostra do 9 até o final
print(frase[9::3]) # Mostra do 9 até o final, pulando de 3 em 3
# ANALISE DE STRINGS
print(len(frase))     # Mostra o tamanho da string, ou seja, quantos caracteres ela tem
print(frase.count('o'))  # Conta quantas vezes o caractere 'o' aparece na string
print(frase.count('o',0,13)) # Conta quantas vezes o caractere 'o' aparece na string, do 0 ao 13 (o 13 não entra)
print(frase.find('deo'))  # Mostra a posição onde começa o trecho 'deo'
print(frase.find('Android')) # Se não encontrar o trecho, retorna -1
# TRANSFORMAÇÃO DE STRINGS
print(frase.replace('Python', 'Android')) # Substitui a palavra Python por Android
print(frase.upper())  # Transforma todos os caracteres em maiúsculo
print(frase.lower())  # Transforma todos os caracteres em minúsculo
print(frase.capitalize()) # Transforma o primeiro caractere em maiúsculo e o resto em minúsculo
print(frase.title())  # Transforma a primeira letra de cada palavra em maiúsculo
# REMOÇÃO DE ESPAÇOS
frase2 = '   Aprenda Python  '
print(frase2.strip())  # Remove os espaços em branco do começo e do fim
print(frase2.rstrip()) # Remove os espaços em branco do fim (R DE RIGHT)
print(frase2.lstrip()) # Remove os espaços em branco do começo (L DE LEFT)
# DIVISÃO E JUNÇÃO DE STRINGS
frase3 = 'Curso em Video Python'
print(frase3.split())  # Divide a string em uma lista de palavras
# JUNÇÃO
frase4 = ['Curso', 'em', 'Video', 'Python']
print(' '.join(frase4))  # Junta a lista de palavras em uma string, separando por espaço


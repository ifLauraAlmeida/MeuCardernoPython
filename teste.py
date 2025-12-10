
num = "12345"

# BÁSICO (sem passo)
print(num[0])           # Output: "1" (índice 0)
print(num[2])           # Output: "3" (índice 2)
print(num[-1])          # Output: "5" (último caractere)
print(num[-2])          # Output: "4" (penúltimo caractere)

# DO INÍCIO ATÉ UM PONTO
print(num[:2])          # Output: "12" (começo até índice 2, o 2 não entra)
print(num[:4])          # Output: "1234" (começo até índice 4, o 4 não entra)
print(num[:-1])         # Output: "1234" (começo até o penúltimo)
print(num[:-2])         # Output: "123" (começo até 2 posições do final)

# DE UM PONTO ATÉ O FINAL
print(num[1:])          # Output: "2345" (do índice 1 até o final)
print(num[3:])          # Output: "45" (do índice 3 até o final)
print(num[-2:])         # Output: "45" (últimas 2 posições)
print(num[-3:])         # Output: "345" (últimas 3 posições)

# ENTRE DOIS PONTOS
print(num[1:3])         # Output: "23" (do 1 ao 3, o 3 não entra)
print(num[0:5])         # Output: "12345" (do 0 ao 5, o 5 não entra)
print(num[1:4])         # Output: "234" (do 1 ao 4, o 4 não entra)
print(num[-4:-1])       # Output: "234" (da 4ª até a penúltima)

# COM PASSO POSITIVO (pulando caracteres)
print(num[::1])         # Output: "12345" (todo com passo 1)
print(num[::2])         # Output: "135" (pega cada 2º caractere)
print(num[::3])         # Output: "14" (pega cada 3º caractere)
print(num[1::2])        # Output: "24" (começando do 1, pega cada 2º)
print(num[0::3])        # Output: "14" (começando do 0, pega cada 3º)

# COM PASSO NEGATIVO (inverte)
print(num[::-1])        # Output: "54321" (inverte tudo)
print(num[::-2])        # Output: "531" (inverte e pega cada 2º)
print(num[::-3])        # Output: "52" (inverte e pega cada 3º)
print(num[4:0:-1])      # Output: "543" (inverte do 4 ao 0, o 0 não entra)
print(num[3::-1])       # Output: "4321" (inverte do 3 até o começo)
print(num[:1:-1])       # Output: "54321" (inverte até o 1, o 1 não entra)
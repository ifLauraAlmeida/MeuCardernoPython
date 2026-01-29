# ============================================
# TRATAMENTO DE ERROS E EXCEÇÕES EM PYTHON
# Curso em Vídeo – Mundo 3
# ============================================

# Em Python, erros em tempo de execução geram EXCEÇÕES.
# Para evitar que o programa quebre, usamos try / except.

# --------------------------------------------
# EXEMPLO 1 – Erro sem tratamento
# --------------------------------------------

# n = int(input("Digite um número: "))
# print(10 / n)
# Se o usuário digitar 0 ou algo que não seja número,
# o programa vai quebrar.

# --------------------------------------------
# EXEMPLO 2 – Tratamento básico com try / except
# --------------------------------------------

try:
    n = int(input("Digite um número: "))
    print(10 / n)
except:
    print("Erro! Algo deu errado.")

# O except captura QUALQUER erro (não é recomendado em projetos grandes)

# --------------------------------------------
# EXEMPLO 3 – Tratando erros específicos
# --------------------------------------------

try:
    n = int(input("Digite um número: "))
    resultado = 10 / n
except ValueError:
    print("Erro: você não digitou um número inteiro.")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
except Exception as erro:
    print(f"Erro inesperado: {erro}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Fim do programa.")

# else → executa se NÃO houver erro
# finally → executa SEMPRE (com erro ou sem erro)

# --------------------------------------------
# EXEMPLO 4 – Validando entrada do usuário
# --------------------------------------------

while True:
    try:
        valor = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Valor inválido. Tente novamente.")
    else:
        print(f"Você digitou {valor}")
        break

# --------------------------------------------
# EXEMPLO 5 – Função com tratamento de erros
# --------------------------------------------

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Não é possível dividir por zero."
    except TypeError:
        return "Digite apenas números."

print(dividir(10, 2))
print(dividir(10, 0))
print(dividir(10, "a"))

# --------------------------------------------
# BOAS PRÁTICAS (Guanabara aprova 👍)
# --------------------------------------------

# ✔ Trate erros específicos
# ✔ Use except genérico só em último caso
# ✔ Sempre dê mensagens claras ao usuário
# ✔ Evite deixar o programa quebrar

# "Errar é humano. Tratar o erro é coisa de programador." 😄

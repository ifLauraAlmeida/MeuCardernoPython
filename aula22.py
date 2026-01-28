"""
AULA 22 – MÓDULOS E PACOTES EM PYTHON
Curso em Vídeo – Gustavo Guanabara (Mundo 3)

OBJETIVO DESTE ARQUIVO:
- Explicar o que são módulos
- Mostrar como criar e importar módulos
- Explicar pacotes
- Demonstrar boas práticas de organização de código
"""

# =========================================================
# 1. O QUE É UM MÓDULO?
# =========================================================
# Um módulo é simplesmente um arquivo .py
# que contém funções, variáveis e/ou classes
# que podem ser reutilizadas em outros programas.

# Exemplo: este próprio arquivo é um módulo.


# =========================================================
# 2. CRIANDO FUNÇÕES (QUE PODERIAM ESTAR EM UM MÓDULO)
# =========================================================

def soma(a, b):
    """
    Retorna a soma de dois números
    """
    return a + b


def subtracao(a, b):
    """
    Retorna a subtração de dois números
    """
    return a - b


def multiplicacao(a, b):
    """
    Retorna a multiplicação de dois números
    """
    return a * b


def divisao(a, b):
    """
    Retorna a divisão de dois números
    """
    if b == 0:
        return "Erro: divisão por zero"
    return a / b


# =========================================================
# 3. COMO ESSE ARQUIVO SERIA USADO COMO MÓDULO
# =========================================================
# Supondo que este arquivo se chame:
# operacoes.py
#
# Em outro arquivo Python, você poderia fazer:
#
# import operacoes
# print(operacoes.soma(2, 3))
#
# OU
#
# from operacoes import soma, multiplicacao
# print(soma(5, 2))


# =========================================================
# 4. USO DO __name__ == "__main__"
# =========================================================
# Isso permite que o arquivo seja:
# - importado como módulo
# - ou executado diretamente

if __name__ == "__main__":
    print("Executando o módulo diretamente")

    print("Soma:", soma(10, 5))
    print("Subtração:", subtracao(10, 5))
    print("Multiplicação:", multiplicacao(10, 5))
    print("Divisão:", divisao(10, 5))


# =========================================================
# 5. O QUE É UM PACOTE?
# =========================================================
# Um pacote é uma PASTA que contém vários módulos.
#
# Estrutura típica:
#
# meu_pacote/
# ├── __init__.py
# ├── numeros.py
# ├── textos.py
#
# O arquivo __init__.py indica que a pasta é um pacote.


# =========================================================
# 6. EXEMPLO DE ORGANIZAÇÃO EM PACOTES (TEORIA)
# =========================================================
"""
Exemplo de pacote chamado 'utilidades':

utilidades/
├── __init__.py
├── numeros.py
├── datas.py

numeros.py:
    def soma(a, b):
        return a + b

datas.py:
    def data_formatada():
        return "27/01/2026"

Uso em outro arquivo:
from utilidades import numeros
print(numeros.soma(2, 3))
"""


# =========================================================
# 7. BOAS PRÁTICAS ENSINADAS NA AULA
# =========================================================
# - Separar código em módulos
# - Evitar arquivos muito grandes
# - Reutilizar funções
# - Organizar projetos grandes com pacotes
# - Usar nomes claros para módulos e funções


# =========================================================
# 8. CONCLUSÃO
# =========================================================
"""
Módulos e pacotes permitem:
✔ Organização
✔ Reutilização de código
✔ Projetos mais profissionais
✔ Manutenção mais fácil
"""

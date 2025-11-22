# ========================================
# FORMATAÇÕES PARA TEXTO EM PYTHON
# ========================================

print("=" * 50)
print("FORMATAÇÕES NUMÉRICAS")
print("=" * 50)

# Números com casas decimais
preco = 49.99
print(f'Preço com 2 casas: R$ {preco:.2f}')
print(f'Preço com 0 casas: R$ {preco:.0f}')
print(f'Preço com 4 casas: R$ {preco:.4f}')

# Números inteiros
numero = 42
print(f'Número inteiro: {numero:d}')
print(f'Número com zeros à esquerda (5 dígitos): {numero:05d}')
print(f'Número com zeros à esquerda (8 dígitos): {numero:08d}')

# Números com separador de milhares
valor = 1500000
print(f'Com separador de milhares: {valor:,}')
print(f'Moeda com separador: R$ {valor:,.2f}')

# Notação científica
grande_numero = 1234567.89
print(f'Notação científica: {grande_numero:e}')
print(f'Notação científica (2 casas): {grande_numero:.2e}')

# Percentual
taxa = 0.25
print(f'Percentual: {taxa:.0%}')
print(f'Percentual (2 casas): {taxa:.2%}')
taxa2 = 0.856
print(f'Percentual: {taxa2:.2%}')

# Hexadecimal, Octal e Binário
numero_hex = 255
print(f'Hexadecimal: {numero_hex:x}')
print(f'Hexadecimal (maiúsculo): {numero_hex:X}')
print(f'Octal: {numero_hex:o}')
print(f'Binário: {numero_hex:b}')

print("\n" + "=" * 50)
print("FORMATAÇÕES DE STRINGS - ALINHAMENTO")
print("=" * 50)

nome = 'Laura'
# Alinhamento à direita
print(f'Direita (20 caracteres): |{nome:>20}|')
# Alinhamento à esquerda
print(f'Esquerda (20 caracteres): |{nome:<20}|')
# Centralizado
print(f'Centralizado (20 caracteres): |{nome:^20}|')

# Com preenchimento customizado
print(f'Direita com asteriscos: |{nome:*>20}|')
print(f'Esquerda com hífen: |{nome:-<20}|')
print(f'Centralizado com ponto: |{nome:.^20}|')

print("\n" + "=" * 50)
print("FORMATAÇÕES DE STRINGS - COMPRIMENTO")
print("=" * 50)

texto_longo = 'Python é uma linguagem de programação poderosa'
# Limitar comprimento
print(f'5 primeiros caracteres: {texto_longo:5}')
print(f'10 primeiros caracteres: {texto_longo:.10}')
print(f'20 primeiros caracteres com reticências: {texto_longo:.20}...')

# Combinando alinhamento e comprimento
print(f'15 caracteres, alinhado direita: |{texto_longo:>15}|')
print(f'10 caracteres máx, centralizado: |{texto_longo:^10}|')

print("\n" + "=" * 50)
print("FORMATAÇÕES COM CASE (maiúsculas/minúsculas)")
print("=" * 50)

palavra = 'Python'
# Usando format com !r (repr), !s (str), !a (ascii)
print(f'String normal: {palavra!s}')
print(f'String com repr: {palavra!r}')
print(f'ASCII: {palavra!a}')

# Combinação de formatações
print(f'Maiúsculas: {palavra.upper()}')
print(f'Minúsculas: {palavra.lower()}')

print("\n" + "=" * 50)
print("FORMATAÇÕES COM VALORES ESPECIAIS")
print("=" * 50)

# Valores booleanos
verdadeiro = True
falso = False
print(f'Booleano 1: {verdadeiro}')
print(f'Booleano 2: {falso}')

# None
nulo = None
print(f'Valor None: {nulo}')

print("\n" + "=" * 50)
print("COMBINAÇÕES AVANÇADAS")
print("=" * 50)

# Combinação: número com percentual, alinhado e com cores
valor_vendas = 0.7856
print(f'Vendas: {valor_vendas:>10.2%}')

# Tabela formatada
print(f'{"Produto":<15} {"Preço":>10} {"Quantidade":>10}')
print('-' * 35)
print(f'{"Notebook":<15} {"R$ 2500.00":>10} {"5":>10}')
print(f'{"Mouse":<15} {"R$ 45.50":>10} {"20":>10}')
print(f'{"Teclado":<15} {"R$ 150.00":>10} {"12":>10}')

# Data e hora
from datetime import datetime
agora = datetime.now()
print(f'\nData e hora: {agora}')
print(f'Data formatada: {agora:%d/%m/%Y}')
print(f'Hora formatada: {agora:%H:%M:%S}')

print("\n" + "=" * 50)
print("REFERÊNCIA RÁPIDA")
print("=" * 50)
print("""
NÚMEROS:
  :.2f     - 2 casas decimais
  :d       - inteiro
  :05d     - inteiro com zeros à esquerda (5 dígitos)
  :,       - separador de milhares
  :.0%     - percentual
  :e       - notação científica
  :x       - hexadecimal
  :b       - binário

STRINGS (alinhamento em N caracteres):
  :>N      - alinhado à direita
  :<N      - alinhado à esquerda
  :^N      - centralizado
  :*>N     - alinhado direita com asteriscos

STRINGS (comprimento):
  :.N      - primeiros N caracteres

COMBINAÇÕES:
  :*>20    - 20 caracteres, alinhado direita, preenchido com *
  :.2%     - percentual com 2 casas decimais
""")

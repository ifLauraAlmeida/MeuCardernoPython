def leiadinheiro(mensagem):
    while True:
        try:
            valor_entrada = input(mensagem).strip()
            
            # Verifica se está vazio
            if not valor_entrada:
                print('ERRO: você não digitou nada! Por favor digite um valor monetário válido!')
                continue
            
            # Tenta converter para float
            valor = float(valor_entrada)
            
            # Verifica se é negativo
            if valor < 0:
                print('ERRO: por favor digite um valor positivo!')
                continue
            
            return valor
        except ValueError:
            print('ERRO: entrada inválida! Por favor digite um valor monetário válido (apenas números e ponto)!')

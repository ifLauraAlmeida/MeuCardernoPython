def leiadinheiro(mensagem):
    while True:
        valor_entrada = input(mensagem).strip()
        
        if not valor_entrada:
            print('ERRO: digite um valor!')
            continue
        
        valido = True
        for caractere in valor_entrada:
            if caractere not in '0123456789.':
                valido = False
                break
        
        if not valido:
            print('ERRO: apenas números e ponto!')
            continue
        
        valor = float(valor_entrada)
        
        if valor < 0:
            print('ERRO: apenas valores positivos!')
            continue
        
        return valor

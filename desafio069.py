# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

c = 1
maioridade = homens = mulheres = mulheresmenores = 0
while True:
    idade = int(input(f"Qual a idade da {c}ª pessoa? "))
    sexo = str(input(f"Qual sexo da {c}ª pessoa [F/M]? ")).upper().strip()

    if 'F' in sexo :
        mulheres += 1
    elif 'M' in sexo:
        homens += 1

    if idade > 18:
        maioridade += 1

    if idade < 20 and 'F' in sexo:
        mulheresmenores += 1

    c += 1
    continuar = str(input("Deseja continuar [S/N]? ")).upper().strip()
    if 'N' in continuar:
        print("=="*15, "RESULTADOS","=="*15)
        print
        print(f"""    Registramos ao todo {maioridade} maiores de 18 anos.
        Registramos também {homens} homens.
        E claro, {mulheresmenores} mulheres menores de 20 anos.""")
        print("=="*40)
        break

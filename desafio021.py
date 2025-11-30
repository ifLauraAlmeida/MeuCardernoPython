#ouvindo um mp3 com python
import pygame as pg

pg.init()

lista = ["laura", "silvana", "gabriel", "morgana", "europa", "marcio", "marcos", "lilian", "marta", "luiz", "marcia", "louise", "nicolas", "loyola", "leonardo"]

while True:
    nome = input("\nDigite um nome (ou 'sair' para encerrar): ").lower()

    if nome == "sair":
        print("Encerrando programa")
        break

    for pessoa in lista:
        if nome == pessoa:
            pg.mixer.music.load(f"{pessoa}.mp3")
            pg.mixer.music.play()
            print(f"Esse áudio me lembra de {pessoa} 🎶")

            while pg.mixer.music.get_busy():
                pg.time.Clock().tick(10)

            break
    else:
        print("Nome não encontrado")

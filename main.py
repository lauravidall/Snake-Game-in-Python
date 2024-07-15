from tkinter import *
import random
import csv

#nome = str(input("Digite o seu nome: "))
# score = int(input("Digite o seu score: "))
# inserindoScore(nome, score)

GAME_WIDTH = 700
GAME_HEIGHT = 700
VELOCIDADE = 50
SPACE_SIZE = 50
BODY_PARTS = 3
COR_COBRA = "#00FF00"
COR_MACA = "#FF0000"
BACKGROUND_COLOR = "#000000"
class Snake: 
    pass
class Maca:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE
        self.coordinates[x,y]

        canvas.create_oval(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill=COR_MACA)

def proxPartida():
    pass

def trocarDirecao(novaDirecao):
    pass

def verificarColisao():
    pass

def gameOver():
    pass

def inserindoScore(nome, score):
    dados = []
    with open("score.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            dados.append([linha[0], int(linha[1])])
    
    inserido = False
    for i in range(len(dados)):
        if score >= dados[i][1]:
            dados.insert(i, [nome, score])
            inserido = True
            break
    
    if not inserido:
        dados.append([nome, score])

    with open("score.csv", "w", newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(dados)

janela = Tk()
janela.title("Snake Game")
janela.resizable(False, False)

score = 0
direcao = "down"

label = Label(janela, text="Score: {}".format(score),font=("consolas",40))
label.pack()

canvas = Canvas(janela, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

janela.update()

janelaWidth = janela.winfo_width()
janelaHeight = janela.winfo_height()
telaWidht = janela.winfo_screenwidth()
telaHeight = janela.winfo_screenheight()

x = int((janelaWidth/2) - (janelaHeight/2))
y = int((telaHeight/2) - (telaWidht/2))

janela.geometry(f"{janelaWidth}x{janelaHeight}+{x}+{y}")

snake = Snake()
maca = Maca()

janela.mainloop()
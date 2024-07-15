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
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=COR_COBRA, tag="snake")
            self.squares.append(square)
class Maca:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = (x, y)
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=COR_MACA, tags="maca")

def proximaVirada(snake, maca):
    x, y = snake.coordinates[0]

    if direcao == "up":
        y -= SPACE_SIZE
    elif direcao == "down":
        y += SPACE_SIZE
    elif direcao == "right":
        x += SPACE_SIZE
    elif direcao == "left":
        x -= SPACE_SIZE

    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=COR_COBRA)
    snake.squares.insert(0, square)

    del snake.coordinates [-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]

    janela.after(VELOCIDADE, proximaVirada, snake, maca)

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

label = Label(janela, text="Score: {}".format(score), font=("consolas", 40))
label.pack()

canvas = Canvas(janela, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

janela.update()

janelaWidth = janela.winfo_width()
janelaHeight = janela.winfo_height()
telaWidht = janela.winfo_screenwidth()
telaHeight = janela.winfo_screenheight()

x = int((telaWidht / 2) - (janelaWidth / 2))
y = int((telaHeight / 2) - (janelaHeight / 2))

janela.geometry(f"{janelaWidth}x{janelaHeight}+{x}+{y}")

snake = Snake()
maca = Maca()

proximaVirada(snake, maca)

janela.mainloop()
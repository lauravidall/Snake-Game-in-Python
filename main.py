from tkinter import *
import random
import csv

class Snake: 
    pass

class Maca:
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

nome = str(input("Digite o seu nome: "))
score = int(input("Digite o seu score: "))

inserindoScore(nome, score)

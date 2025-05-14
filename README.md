# 🐍 Snake Game em Python

Este é um simples jogo da cobrinha (Snake) implementado com `Python` e `tkinter`. O objetivo é controlar a cobra para comer maçãs, aumentando seu tamanho e sua pontuação. O jogo termina quando a cobra colide com as paredes ou com ela mesma.

## 🎮 Como Jogar

- Use as teclas de direção (setas) para mover a cobra para cima, baixo, esquerda ou direita.
- Cada vez que a cobra come uma maçã, ela cresce e sua pontuação aumenta.
- O jogo termina se a cobra colidir com as paredes ou com ela mesma.

## 🚀 Requisitos

- Python 3
- Biblioteca `tkinter` (geralmente já inclusa com a instalação do Python)

## 🧑‍💻 Como Rodar o Jogo

1. Clone este repositório ou baixe o código Python.
2. Abra o terminal ou prompt de comando.
3. Navegue até o diretório onde o arquivo `snake_game.py` está localizado.
4. Execute o seguinte comando:

    ```bash
    python main.py
    ```

5. O jogo será iniciado em uma janela gráfica.

## 🛠️ Como Funciona

### Estrutura do Código

O código é dividido em algumas partes principais:

- **Classe Snake**: Responsável pela criação e movimentação da cobra.
- **Classe Maca**: Responsável pela criação e posicionamento aleatório das maçãs.
- **Funções de Movimento e Colisão**:
  - A cobra se move com base nas teclas pressionadas e cresce ao comer maçãs.
  - O jogo verifica se há colisões com as paredes ou com o próprio corpo da cobra.
  - Quando a cobra come uma maçã, a pontuação aumenta e a maçã é reposicionada aleatoriamente.

### Componentes Principais

- **Tela de Jogo**: Criada com `tkinter.Canvas` para exibir a cobra, a maçã e o fundo do jogo.
- **Controle de Teclado**: As teclas de direção (esquerda, direita, cima, baixo) são usadas para controlar o movimento da cobra.
- **Pontuação**: A pontuação é exibida no topo da tela e aumentada a cada maçã comida.
- **Botão de Reiniciar**: Um botão é exibido para reiniciar o jogo a qualquer momento.

### Funções Importantes

- `nextTurn(snake, maca)`: Controla o movimento da cobra e a lógica do jogo (crescimento, colisões, reinício).
- `trocarDirecao(novaDirecao)`: Altera a direção da cobra com base nas teclas pressionadas.
- `verificarColisao(snake)`: Verifica se a cobra colidiu com as paredes ou com seu próprio corpo.
- `gameOver()`: Exibe a tela de Game Over e para o jogo.
- `restartGame()`: Reinicia o jogo com os parâmetros iniciais.

## 🔧 Personalização

Você pode personalizar o jogo alterando as variáveis de configuração:

- `GAME_WIDTH` e `GAME_HEIGHT`: Definem o tamanho da tela do jogo.
- `VELOCIDADE`: Controla a velocidade do jogo.
- `SPACE_SIZE`: Define o tamanho das células (tanto da cobra quanto das maçãs).
- `COR_COBRA` e `COR_MACA`: Definem as cores da cobra e da maçã, respectivamente.
- `BACKGROUND_COLOR`: Define a cor de fundo do jogo.

Sinta-se à vontade para contribuir com melhorias, sugestões ou correções para este projeto! Basta fazer um fork do repositório e criar um pull request.

---


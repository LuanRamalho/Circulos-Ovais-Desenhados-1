import tkinter as tk
import random

def desenhar_circulos_ovais():
    # Dimensões da tela
    largura = 800
    altura = 600

    # Criação da janela principal
    janela = tk.Tk()
    janela.title("Círculos Ovais Aleatórios")

    # Criação do canvas
    canvas = tk.Canvas(janela, width=largura, height=altura, bg="white")
    canvas.pack()

    # Geração de uma quantidade aleatória de círculos ovais
    quantidade = random.randint(10, 50)  # Quantidade entre 10 e 50

    for _ in range(quantidade):
        # Coordenadas aleatórias para os círculos ovais
        x1 = random.randint(0, largura - 100)
        y1 = random.randint(0, altura - 100)
        x2 = x1 + random.randint(20, 100)
        y2 = y1 + random.randint(20, 100)

        # Cor aleatória
        cor = f"#{random.randint(0, 0xFFFFFF):06x}"

        # Desenho do oval
        canvas.create_oval(x1, y1, x2, y2, fill=cor, outline="")

    # Início do loop principal
    janela.mainloop()

# Executar a função
desenhar_circulos_ovais()

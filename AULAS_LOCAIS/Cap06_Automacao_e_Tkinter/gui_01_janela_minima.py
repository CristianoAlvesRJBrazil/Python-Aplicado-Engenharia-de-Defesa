"""
gui_01_janela_minima.py — A janela mínima em Tkinter (Listagem 6.7).

  RODE NA MÁQUINA LOCAL:  python3 gui_01_janela_minima.py
  (NÃO funciona no Google Colab: o navegador não tem tela gráfica.)

Todo programa Tkinter segue o mesmo esqueleto: cria-se a janela principal,
adicionam-se os widgets e entra-se no laço de eventos com mainloop(), que
mantém a janela aberta e atenta às ações do usuário.
"""

import tkinter as tk

janela = tk.Tk()                 # cria a janela principal
janela.title("Sistema de Monitoramento")

rotulo = tk.Label(janela, text="Olá, operador!")
rotulo.pack(padx=20, pady=20)    # posiciona o widget na janela

if __name__ == "__main__":
    janela.mainloop()            # inicia o laço de eventos

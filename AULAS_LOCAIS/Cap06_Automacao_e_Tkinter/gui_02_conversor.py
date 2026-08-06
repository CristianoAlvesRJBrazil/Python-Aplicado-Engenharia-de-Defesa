"""
gui_02_conversor.py — Conversor de velocidade com interface gráfica (Listagem 6.8).

  RODE NA MÁQUINA LOCAL:  python3 gui_02_conversor.py
  (NÃO funciona no Google Colab: o navegador não tem tela gráfica.)

Reúne três ideias: um Entry guarda o que o usuário digita (lido com .get());
o parâmetro command=converter liga o botão à função (SEM parênteses — ela
será chamada pelo Tkinter no clique); e resultado.config(...) atualiza o
texto de um widget já existente — a forma de a interface "responder".
"""

import tkinter as tk


def converter():
    """Callback do botão: lê o campo, converte e mostra o resultado."""
    try:
        nos = float(campo.get())          # lê o texto digitado
        resultado.config(text=f"{nos * 1.852:.1f} km/h")
    except ValueError:
        resultado.config(text="Valor inválido")


janela = tk.Tk()
janela.title("Conversor de velocidade")

tk.Label(janela, text="Velocidade em nós:").pack(padx=10, pady=(10, 0))
campo = tk.Entry(janela)
campo.pack(padx=10, pady=5)

tk.Button(janela, text="Converter", command=converter).pack(pady=5)
resultado = tk.Label(janela, text="...", font=("Helvetica", 14))
resultado.pack(pady=(0, 10))

if __name__ == "__main__":
    janela.mainloop()

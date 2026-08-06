"""
gui_03_monitor_ocorrencias.py — Interface do miniprojeto, Módulo 3 (Listagem 6.13).

  RODE NA MÁQUINA LOCAL:  python3 gui_03_monitor_ocorrencias.py
  (NÃO funciona no Google Colab: o navegador não tem tela gráfica.)

Uma janela pela qual o operador registra ocorrências e acompanha, em tempo
real, a lista de alertas — reutilizando SEM alterar a classe
RegistroDeOcorrencias do Capítulo 5 (arquivo registro.py, na mesma pasta).
A interface não sabe COMO um alerta é determinado: apenas chama
registro.registrar(...) e registro.alertas(). Toda a lógica vive no núcleo.
"""

import tkinter as tk
from tkinter import messagebox

from registro import RegistroDeOcorrencias   # classe do Capítulo 5

registro = RegistroDeOcorrencias(limite=40.0)


def registrar():
    """Lê os campos, registra a ocorrência e atualiza a lista."""
    sensor = campo_sensor.get().strip()
    try:
        velocidade = float(campo_velocidade.get())
    except ValueError:
        messagebox.showerror("Erro", "Velocidade inválida.")
        return
    if not sensor:
        messagebox.showerror("Erro", "Informe o sensor.")
        return
    registro.registrar(sensor, velocidade)
    campo_sensor.delete(0, tk.END)
    campo_velocidade.delete(0, tk.END)
    atualizar_lista()


def atualizar_lista():
    """Recarrega a lista de alertas a partir do registro."""
    lista.delete(0, tk.END)
    for o in registro.alertas():
        lista.insert(tk.END, f"#{o.id}  {o.sensor}  -  {o.velocidade_kmh} km/h")


# ---- Montagem da janela ----
janela = tk.Tk()
janela.title("Monitor de Ocorrências")

tk.Label(janela, text="Sensor:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
campo_sensor = tk.Entry(janela, width=30)
campo_sensor.grid(row=0, column=1, padx=5, pady=5)

tk.Label(janela, text="Velocidade (km/h):").grid(row=1, column=0, sticky="e", padx=5)
campo_velocidade = tk.Entry(janela, width=30)
campo_velocidade.grid(row=1, column=1, padx=5)

tk.Button(janela, text="Registrar", command=registrar).grid(
    row=2, column=0, columnspan=2, pady=8)

tk.Label(janela, text="Ocorrências em alerta:").grid(
    row=3, column=0, columnspan=2)
lista = tk.Listbox(janela, width=45, height=6)
lista.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

if __name__ == "__main__":
    janela.mainloop()

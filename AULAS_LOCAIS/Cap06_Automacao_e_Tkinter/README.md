# Capítulo 6 — Automação, Módulos e Tkinter (código local)

Estes arquivos **rodam na sua máquina**, não no Google Colab. O Tkinter abre
**janelas gráficas**, e o Colab (por executar no navegador) não tem tela para
exibi-las. Use o ambiente local (Anaconda/`venv` + VS Code) do Capítulo 1.

## Requisitos
- **Python 3.10+** com **Tkinter** (a maioria das instalações já o inclui).
  - Windows / macOS (instalador oficial ou Anaconda): já vem com Tkinter.
  - Linux, se faltar: `sudo apt install python3-tk`
- Teste rápido: `python3 -m tkinter` deve abrir uma janelinha de demonstração.

## Como rodar
Abra um terminal **nesta pasta** e execute:

```bash
python3 registro.py               # núcleo (Cap. 5): teste sem interface
python3 conversoes.py             # módulo próprio + if __name__ == "__main__"
python3 automacao_pathlib.py      # automação com pathlib (cria logs/ de amostra)

python3 gui_01_janela_minima.py   # a janela mínima em Tkinter
python3 gui_02_conversor.py       # conversor nós -> km/h com botão
python3 gui_03_monitor_ocorrencias.py   # interface do miniprojeto (Módulo 3)
```

Feche a janela para encerrar cada programa gráfico.

## Os arquivos

| Arquivo | Listagem no livro | O que é |
|---|---|---|
| `registro.py` | Cap. 5 | Classes `Ocorrencia` e `RegistroDeOcorrencias` — o **núcleo**, reaproveitado sem alteração pela interface |
| `conversoes.py` | 6.3–6.5 | Módulo próprio de conversões, com bloco de teste `if __name__ == "__main__"` |
| `automacao_pathlib.py` | 6.1–6.2 | Automação: varre uma pasta de `.txt` e consolida um `resumo.txt` (cria `logs/` de amostra) |
| `gui_01_janela_minima.py` | 6.7 | O esqueleto de todo programa Tkinter: `Tk()` → widgets → `mainloop()` |
| `gui_02_conversor.py` | 6.8 | `Entry` + `Button` + *callback*; lê o campo, converte e responde |
| `gui_03_monitor_ocorrencias.py` | 6.13 | Miniprojeto (Módulo 3): registra ocorrências e lista alertas, importando `registro.py` |

## Detalhe de projeto
Nos arquivos de interface, a chamada `janela.mainloop()` fica dentro de
`if __name__ == "__main__":`. Assim, o arquivo pode ser **executado** (abre a
janela) ou **importado** (reaproveitar/testar os widgets e *callbacks*) sem
disparar o laço de eventos — o mesmo idioma de módulo ensinado na Seção 6.2.

A interface (`gui_03`) **não contém regra de negócio**: ela apenas chama
`registro.registrar(...)` e `registro.alertas()`. Toda a lógica vive em
`registro.py`. Trocar o Tkinter por outra biblioteca não exigiria tocar no
núcleo — a separação entre lógica e apresentação em ação.

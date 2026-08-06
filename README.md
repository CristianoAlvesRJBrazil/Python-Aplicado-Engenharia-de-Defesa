# Programação com Python Aplicada à Engenharia de Defesa

Materiais de apoio do livro-texto **_Programação com Python Aplicada à Engenharia
de Defesa_**, de **Cristiano da Costa Alves** — um curso prático de 40 horas,
organizado em quatro módulos, com foco em aplicações reais de defesa e segurança
nacional.

Este repositório reúne os **notebooks de aula** (prontos para o Google Colab) e uma
**amostra gratuita do livro** (Capítulos 1 a 3). O livro completo é distribuído à
parte; aqui ficam os materiais de código, sob licença aberta.

---

## 📓 Notebooks de aula (Google Colab)

Um notebook por capítulo, executável no navegador, sem nenhuma instalação. Abra-o ao
lado do texto e execute cada trecho de código à medida que ele aparece — programação
se aprende com as mãos no teclado.

| Capítulo | Tema | Abrir no Colab |
|---|---|---|
| 1 | Engenharia de Defesa e Programação | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CristianoAlvesRJBrazil/Python-Aplicado-Engenharia-de-Defesa/blob/main/AULAS_COLAB/Cap01_Engenharia_de_Defesa_e_Programacao.ipynb) |
| 2 | Fundamentos de Python | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CristianoAlvesRJBrazil/Python-Aplicado-Engenharia-de-Defesa/blob/main/AULAS_COLAB/Cap02_Fundamentos_de_Python.ipynb) |
| 3 | Estruturas de Dados Nativas | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CristianoAlvesRJBrazil/Python-Aplicado-Engenharia-de-Defesa/blob/main/AULAS_COLAB/Cap03_Estruturas_de_Dados_Nativas.ipynb) |
| 4 | Persistência, Expressões Regulares e Tratamento de Erros | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CristianoAlvesRJBrazil/Python-Aplicado-Engenharia-de-Defesa/blob/main/AULAS_COLAB/Cap04_Persistencia_Regex_Erros.ipynb) |
| 5 | Programação Orientada a Objetos | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/CristianoAlvesRJBrazil/Python-Aplicado-Engenharia-de-Defesa/blob/main/AULAS_COLAB/Cap05_Programacao_Orientada_a_Objetos.ipynb) |

> Os notebooks acompanham o **miniprojeto integrador** — um pequeno sistema de apoio
> à decisão, construído passo a passo ao longo do curso.

## 🖥️ Scripts locais (Capítulo 6 — Tkinter)

O Capítulo 6 usa **interface gráfica (Tkinter)**, que **não roda no Colab** (o
navegador não tem tela para abrir janelas). Por isso, esse capítulo vem como
**scripts `.py` para rodar na sua máquina**, em
[AULAS_LOCAIS/Cap06_Automacao_e_Tkinter/](AULAS_LOCAIS/Cap06_Automacao_e_Tkinter/):

```bash
cd AULAS_LOCAIS/Cap06_Automacao_e_Tkinter
python3 gui_03_monitor_ocorrencias.py    # interface do miniprojeto (Módulo 3)
```

Requer Python 3.10+ com Tkinter (no Linux, se faltar: `sudo apt install python3-tk`).
Veja o [README da pasta](AULAS_LOCAIS/Cap06_Automacao_e_Tkinter/README.md) para a
lista completa de scripts e instruções.

## 📄 Amostra do livro

- **[pdf/Amostra-Livro-Capitulos-1-a-3.pdf](pdf/Amostra-Livro-Capitulos-1-a-3.pdf)** —
  Módulo 1 completo (Capítulos 1 a 3), para leitura e avaliação.

O livro completo abrange nove capítulos, em quatro módulos: fundamentos e estruturas
de dados; persistência e orientação a objetos; bibliotecas científicas (NumPy,
pandas, Matplotlib); e um projeto final integrador.

## 🚀 Como usar

1. Clique no selo **Abrir no Colab** do capítulo desejado.
2. No Colab, execute as células **na ordem** (menu *Ambiente de execução → Executar tudo*).
3. Sem acesso à internet? Baixe o `.ipynb` e abra no Jupyter local (Anaconda/`venv`).

Requisitos: nenhum para o Colab. Localmente, Python 3.12+ (apenas a biblioteca padrão
é usada nos capítulos desta amostra).

## 📁 Estrutura

```
.
├── AULAS_COLAB/                            # notebooks de aula (um por capítulo) — publicado
│   ├── Cap01_Engenharia_de_Defesa_e_Programacao.ipynb
│   ├── Cap02_Fundamentos_de_Python.ipynb
│   ├── Cap03_Estruturas_de_Dados_Nativas.ipynb
│   ├── Cap04_Persistencia_Regex_Erros.ipynb
│   └── Cap05_Programacao_Orientada_a_Objetos.ipynb
├── AULAS_LOCAIS/                           # scripts .py para rodar na máquina — publicado
│   └── Cap06_Automacao_e_Tkinter/          #   automação, módulos e GUIs Tkinter
├── pdf/                                    # PDFs gerados
│   └── Amostra-Livro-Capitulos-1-a-3.pdf   #   -> único PDF publicado (Módulo 1)
├── livro/                                  # fontes LaTeX + assets (NÃO publicado)
├── LICENSE
└── README.md
```

> Apenas `AULAS_COLAB/`, a amostra em `pdf/` e este README/LICENSE são versionados.
> As fontes LaTeX do livro completo (`livro/`) e os PDFs integrais (`pdf/main*.pdf`,
> `pdf/cristiano_alves_python_defesa.pdf`) ficam fora do controle de versão.

## 📜 Licença

Código e notebooks sob licença **MIT** (veja [LICENSE](LICENSE)). O texto do livro é
© 2026 Cristiano da Costa Alves; a amostra é disponibilizada para uso didático.

## ✍️ Autor

**Cristiano da Costa Alves** — Quantum Strategic AI · Rio de Janeiro, 2026.
Sugestões e correções são bem-vindas via *issues* deste repositório.

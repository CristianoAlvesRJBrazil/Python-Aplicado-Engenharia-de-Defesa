"""
automacao_pathlib.py — Automação de tarefas repetitivas (Seção 6.1).

Consolida, em um único arquivo (resumo.txt), o total de linhas de cada
arquivo .txt de uma pasta de logs — um pequeno relatório de ingestão.

Para que o exemplo "simplesmente rode", o script CRIA uma pasta 'logs/' com
alguns arquivos de amostra na primeira execução. Em uso real, basta apontar
para a sua própria pasta de logs.

Não usa interface gráfica: roda tanto localmente quanto no Colab.
"""

from pathlib import Path


def criar_logs_de_amostra(pasta):
    """Cria uma pasta de logs de amostra, apenas se ela ainda não existir."""
    if pasta.exists():
        return
    pasta.mkdir(parents=True)
    amostras = {
        "sensor_a1.txt": "linha 1\nlinha 2\nlinha 3\n",
        "sensor_b2.txt": "linha 1\nlinha 2\n",
        "sonar_1.txt": "linha 1\nlinha 2\nlinha 3\nlinha 4\n",
    }
    for nome, conteudo in amostras.items():
        with open(pasta / nome, "w", encoding="utf-8") as f:
            f.write(conteudo)
    print(f"Pasta de amostra criada em '{pasta}/' com {len(amostras)} arquivos.")


def consolidar(pasta, saida="resumo.txt"):
    """Grava, em 'saida', o total de linhas de cada .txt de 'pasta'."""
    relatorio = []
    for arquivo in sorted(pasta.glob("*.txt")):
        with open(arquivo, "r", encoding="utf-8") as f:
            n = len(f.readlines())
        relatorio.append(f"{arquivo.name}: {n} linhas")

    with open(saida, "w", encoding="utf-8") as f:
        f.write("\n".join(relatorio))

    print(f"Resumo de {len(relatorio)} arquivos gravado em '{saida}'.")
    return relatorio


if __name__ == "__main__":
    pasta = Path("logs")
    criar_logs_de_amostra(pasta)

    # Varre a pasta, arquivo por arquivo (Listagem 6.1)
    for arquivo in pasta.glob("*.txt"):
        print(f"Processando {arquivo.name}...")
        with open(arquivo, "r", encoding="utf-8") as f:
            linhas = f.readlines()
        print(f"  {len(linhas)} linhas lidas.")

    # Consolida tudo em um resumo (Listagem 6.2)
    print("-" * 30)
    for linha in consolidar(pasta):
        print(linha)

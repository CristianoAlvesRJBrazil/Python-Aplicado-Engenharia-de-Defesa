"""
conversoes.py — Um módulo próprio (Seção 6.2).

Funções de conversão de unidades para o domínio de defesa. Importe-as de
outro arquivo (`from conversoes import nos_para_kmh`) ou rode este arquivo
diretamente (`python3 conversoes.py`) para o teste rápido do bloco final.
"""


def nos_para_kmh(nos):
    """Converte uma velocidade de nós para km/h (1 nó = 1,852 km/h)."""
    return nos * 1.852


def pes_para_metros(pes):
    """Converte uma altitude de pés para metros (1 pé = 0,3048 m)."""
    return pes * 0.3048


# Este bloco só executa se o arquivo for rodado diretamente,
# não quando ele é importado por outro módulo.
if __name__ == "__main__":
    print("Teste rápido de conversoes.py")
    print(f"  18 nós = {nos_para_kmh(18):.1f} km/h")
    print(f"  35000 pés = {pes_para_metros(35000):.0f} m")

"""
registro.py — Núcleo do miniprojeto (Capítulo 5).

Contém as classes Ocorrencia e RegistroDeOcorrencias, reaproveitadas SEM
alteração pela interface gráfica do Capítulo 6. É a separação de
responsabilidades em ação: a lógica do sistema vive aqui; a interface (em
interface_monitor.py / gui_03_monitor_ocorrencias.py) apenas a aciona.

Este arquivo é um MÓDULO: pode ser importado (`from registro import ...`) ou
executado diretamente (`python3 registro.py`) para um teste rápido.
"""

import json


class Ocorrencia:
    """Uma ocorrência de monitoramento."""

    def __init__(self, id, sensor, velocidade_kmh, tipo="superfície"):
        self.id = id
        self.sensor = sensor
        self.velocidade_kmh = velocidade_kmh
        self.tipo = tipo

    def em_alerta(self, limite=40.0):
        return self.velocidade_kmh > limite

    def para_dict(self):
        """Converte o objeto em dicionário (para o JSON)."""
        return {
            "id": self.id, "sensor": self.sensor,
            "velocidade_kmh": self.velocidade_kmh, "tipo": self.tipo,
        }

    @classmethod
    def de_dict(cls, d):
        """Cria uma Ocorrencia a partir de um dicionário."""
        return cls(d["id"], d["sensor"], d["velocidade_kmh"],
                   d.get("tipo", "superfície"))

    def __repr__(self):
        return f"Ocorrencia(#{self.id}, {self.sensor}, {self.velocidade_kmh} km/h)"


class RegistroDeOcorrencias:
    """Gerencia a coleção de ocorrências e a sua persistência."""

    def __init__(self, limite=40.0):
        self._ocorrencias = []
        self.limite = limite

    def registrar(self, sensor, velocidade_kmh, tipo="superfície"):
        novo_id = len(self._ocorrencias) + 1
        ocorrencia = Ocorrencia(novo_id, sensor, velocidade_kmh, tipo)
        self._ocorrencias.append(ocorrencia)
        return ocorrencia

    def alertas(self):
        return [o for o in self._ocorrencias if o.em_alerta(self.limite)]

    def total(self):
        return len(self._ocorrencias)

    def salvar(self, caminho):
        dados = [o.para_dict() for o in self._ocorrencias]
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)

    def carregar(self, caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)
            self._ocorrencias = [Ocorrencia.de_dict(d) for d in dados]
        except FileNotFoundError:
            self._ocorrencias = []


# Só executa quando este arquivo é rodado diretamente, não na importação.
if __name__ == "__main__":
    registro = RegistroDeOcorrencias(limite=40.0)
    registro.registrar("Radar-A1", 44.4)
    registro.registrar("Sonar-1", 18.5, tipo="submarino")
    registro.registrar("Radar-B2", 50.0, tipo="aéreo")

    print(f"Total de ocorrências: {registro.total()}")
    print("Em alerta:")
    for o in registro.alertas():
        print(f"  {o}")

from enum import Enum
from missao import Mission

class Status(Enum):
    vivo = 1
    desacordado = 2
    morto = 3

class Character:
    def __init__(self, nome: str) -> None:
        self._nome: str = ""

        self._nivel: int = 1
        self._xp: int = 0

        self._vida_maxima = 100
        self._vida: int = self._vida_maxima

        self._missoes: list[Mission] = []

        self.nome = nome

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, value: str):
        if value is None:
            raise ValueError("Can't set None type for this attribute")
        self._nome = value

    @property
    def nivel(self):
        return self._nivel

    @property
    def xp(self):
        return self._xp

    @property
    def vida(self):
        return self._vida

    @property
    def missoes(self):
        return self._missoes

    @missoes.setter
    def missoes(self, mission: Mission):
        self._missoes.append(mission)

    def __str__(self) -> str:
        parts = []
        for attr, val in vars(self).items():
            parts.append(f"{attr}: {val} - ")
        string: str = " ".join(parts)
        return string

    def __eq__(self, value) -> bool:
        if not isinstance(value, Character):
            return False

        if self._nome != value.nome:
            return False

        return True

    def show(self):
        for attr, val in vars(self).items():
            print(f"{attr}: {val}")

    def _modificar_vida(self, cura_dano: int):
        if cura_dano + self._vida > 100:
            self._vida = self._vida_maxima
        else:
            self._vida += cura_dano

        if self._vida > 0:
            self._status = Status.vivo
        elif self._vida <= 0:
            self._status = Status.desacordado
        elif self._vida < -10:
            self._status = Status.morto

    def add_mission(self, mission: Mission):
        mission.iniciar_missao()
        self.missoes = mission

    def finish_mission(self, mission: Mission, val: int):
        if mission not in self.missoes:
            raise ValueError("Missao não foi adicionada ao personagem")

        try:
            mission.concluir_missao(val)
        except ValueError :
             raise # reraise the error 

        self._xp += mission.recompensa
        print(f"recompensa obtida com sucesso. Experência do personagem agora é {self.xp}")

    def show_missions(self):
        for m in self.missoes:
            print(f"{m.nome}, {m.status}")

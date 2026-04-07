from enum import Enum


class Status(Enum):
    pendente = 1
    em_andamento = 2
    concluido = 3


class Mission:
    def __init__(self, nome: str, descric: str, recomp: int) -> None:
        self._nome: str = nome
        self._descricao: str = descric
        self._recompensa: int = recomp
        self._status: Status = Status.pendente

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def descricao(self) -> str:
        return self._descricao

    @property
    def recompensa(self) -> int:
        return self._recompensa

    @property
    def status(self) -> Status:
        return self._status

    @nome.setter
    def nome(self, value: str):
        if value is None:
            raise ValueError("Can't set None type for this attribute")

        value = " ".join(value.split())

        self._nome = value

    @descricao.setter
    def descricao(self, value: str):
        if value is None:
            raise ValueError("Can't set None type for this attribute")
        self._descricao = value

    @recompensa.setter
    def recompensa(self, value: int):
        if value is None:
            raise ValueError("Can't set None type for this attribute")

        if not (1 <= value <= 50):
            raise ValueError("Valor deve estar no período 1 <= n <= 50")

        self._recompensa = value

    @status.setter
    def status(self, value: Status):
        if value is None:
            raise ValueError("Can't set None type for this attribute")

        if not isinstance(value, Status):
            raise ValueError("Valor informado não é do tipo Status")

        next = self._status.value + 1
        if next != value:
            raise ValueError("Valor informado para status não segue o fluxo adequado")

        self._status = value

    def __str__(self) -> str:
        parts = []
        for attr, val in vars(self).items():
            parts.append(f"{attr}: {val} - ")
        string: str = " ".join(parts)
        return string

    def __eq__(self, value) -> bool:
        if not isinstance(value, Mission):
            return False

        if self._nome != value.nome:
            return False

        if self._descricao != value.descricao:
            return False

        if self._recompensa != value.recompensa:
            return False

        return True

    def show(self):
        for attr, val in vars(self).items():
            print(f"{attr}: {val}")

    def iniciar_missao(self):
        if self.status == Status.em_andamento:
            raise ValueError("Missão já em andamento")
        elif self.status == Status.concluido:
            raise ValueError("Missão já concluída")

        self.status = Status.em_andamento

        print(
            f"A missão {self.nome} começou! Objetivo central da missao: {self.descricao}"
        )

    def concluir_missao(self):
        if self.status == Status.pendente:
            raise ValueError("Missão ainda pendente")
        elif self.status == Status.concluido:
            raise ValueError("Missão já concluída")

        self.status = Status.em_andamento

        print(
            f"Missão concluída como sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira."
        )

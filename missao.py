from enum import Enum
from abc import ABC, abstractmethod


class Status(Enum):
    pendente = 1
    em_andamento = 2
    concluido = 3                 


class Mission(ABC):
    def __init__(self, nome: str, descricao: str, recompensa: int) -> None:
        self._nome: str = ""
        self._descricao: str = ""
        self._recompensa: int = 0
        self._status: Status = Status.pendente

        self.nome = nome
        self.descricao = descricao
        self.recompensa = recompensa

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
    def status(self, status: Status):
        if status is None:
            raise ValueError("Can't set None type for this attribute")

        if not isinstance(status, Status):
            raise ValueError("Valor informado não é do tipo Status")

        next = self._status.value + 1
        if next != status.value:
            raise ValueError("Valor informado para status não segue o fluxo adequado")

        self._status = status

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

    @abstractmethod
    def iniciar_missao(self):
        pass

    @abstractmethod
    def concluir_missao(self, req):
        pass

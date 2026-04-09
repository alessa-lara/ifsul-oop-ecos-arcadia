from typing import override
from missao import Mission, Status


class CombatMission(Mission):
    def __init__(
        self,
        nome: str,
        descric: str,
        recomp: int,
        tipo_inimigo: str,
        inimigos_a_derrotar: int,
    ) -> None:
        super().__init__(nome, descric, recomp)

        # var privadas
        self.__tipo_inimigo: str = ""
        self.__inimigos_a_derrotar: int = 0

        # init var com setter
        self.tipo_inimigo = tipo_inimigo
        self.inimigos_a_derrotar = inimigos_a_derrotar

    @property
    def tipo_inimigo(self) -> str:
        return self.__tipo_inimigo

    @property
    def inimigos_a_derrotar(self) -> int:
        return self.__inimigos_a_derrotar

    @tipo_inimigo.setter
    def tipo_inimigo(self, value: str):
        self.__tipo_inimigo = value

    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, value: int):
        self.__inimigos_a_derrotar = value

    @override
    def concluir_missao(self, req: float):
        if self.status == Status.pendente:
            raise ValueError("Missão ainda pendente")
        elif self.status == Status.concluido:
            raise ValueError("Missão já concluída")

        if self.inimigos_a_derrotar > req:
            raise ValueError(
                f"Falta ainda {self.inimigos_a_derrotar - req} para percorrer."
            )

        self.status: Status = Status.concluido

        print(
            f"Missão concluída como sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira."
        )


class GatheringMission(Mission):
    def __init__(
        self,
        nome: str,
        descric: str,
        recomp: int,
        item_necessario: str,
        quantidade_item: int,
    ) -> None:
        super().__init__(nome, descric, recomp)

        # var privadas
        self.__item_necessario: str = ""
        self.__quantidade_item: int = 0

        # init var com setter
        self.item_necessario = item_necessario
        self.quantidade_item = quantidade_item

    @property
    def item_necessario(self) -> str:
        return self.__item_necessario

    @property
    def quantidade_item(self) -> int:
        return self.__quantidade_item

    @item_necessario.setter
    def item_necessario(self, value: str):
        self.__item_necessario = value

    @quantidade_item.setter
    def quantidade_item(self, value: int):
        self.__quantidade_item = value

    @override
    def concluir_missao(self, req: float):
        if self.status == Status.pendente:
            raise ValueError("Missão ainda pendente")
        elif self.status == Status.concluido:
            raise ValueError("Missão já concluída")

        if self.quantidade_item > req:
            raise ValueError(
                f"Falta ainda {self.quantidade_item - req} para percorrer."
            )

        self.status: Status = Status.concluido

        print(
            f"Missão concluída como sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira."
        )


class ExplorationMission(Mission):
    def __init__(
        self,
        nome: str,
        descric: str,
        recomp: int,
        regiao_destino: str,
        distancia_km: float,
    ) -> None:
        super().__init__(nome, descric, recomp)

        # var privadas
        self.__regiao_destino: str = ""
        self.__distancia_km: float = 0

        # init var com setter
        self.regiao_destino = regiao_destino
        self.distancia_km = distancia_km

    @property
    def regiao_destino(self) -> str:
        return self.__regiao_destino

    @property
    def distancia_km(self) -> float:
        return self.__distancia_km

    @regiao_destino.setter
    def regiao_destino(self, value: str):
        self.__regiao_destino = value

    @distancia_km.setter
    def distancia_km(self, value: float):
        self.__distancia_km = value

    @override
    def concluir_missao(self, req: float):
        if self.status == Status.pendente:
            raise ValueError("Missão ainda pendente")
        elif self.status == Status.concluido:
            raise ValueError("Missão já concluída")

        if self.distancia_km > req:
            raise ValueError(f"Falta ainda {self.distancia_km - req} para percorrer.")

        self.status: Status = Status.concluido

        print(
            f"Missão concluída como sucesso. A contabilidade do prêmio de {self.recompensa} XP agora está pronta para retirada financeira."
        )

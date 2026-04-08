from missao import Mission


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
        self.__tipo_inimigo: str = tipo_inimigo
        self.__inimigos_a_derrotar: int = inimigos_a_derrotar

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
        self.__item_necessario = item_necessario
        self.__quantidade_item = quantidade_item

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
        self.__regiao_destino = regiao_destino
        self.__distancia_km = distancia_km

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

class Character:
    def __init__(self, nome: str) -> None:
        self._nome: str = nome
        self._nivel: int = 1
        self._xp: int = 0
        self._vida: int = 100

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

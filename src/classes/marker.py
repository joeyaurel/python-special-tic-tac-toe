class Marker:

    def __init__(self, character: str) -> None:
        self.__character: str = character

    @property
    def character(self) -> str:
        return self.__character

    @character.setter
    def character(self, character: str) -> None:
        self.__character = character.upper() if len(character) == 1 else NullMarker().character


class NullMarker(Marker):

    def __init__(self) -> None:
        super().__init__('?')

    @property
    def character(self) -> str:
        return super().character

    @character.setter
    def character(self, character: str) -> None:
        pass

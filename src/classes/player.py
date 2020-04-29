from .colors import ASCII_COLOR_WHITE
from .marker import Marker, NullMarker


class Player:

    def __init__(self, name: str = '', marker: Marker = NullMarker(), color: str = ASCII_COLOR_WHITE) -> None:
        self.__name = name
        self.__marker = marker
        self.__color = color

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def marker(self) -> Marker:
        return self.__marker

    @marker.setter
    def marker(self, marker: Marker) -> None:
        self.__marker = marker

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str) -> None:
        self.__color = color


class NullPlayer(Player):

    def __init__(self) -> None:
        super().__init__('', NullMarker(), ASCII_COLOR_WHITE)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        pass

    @property
    def marker(self) -> Marker:
        return super().marker

    @marker.setter
    def marker(self, marker: Marker) -> None:
        pass

    @property
    def color(self) -> str:
        return super().color

    @color.setter
    def color(self, color: str) -> None:
        pass

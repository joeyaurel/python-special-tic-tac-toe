from .player import Player, NullPlayer


class Cell:

    def __init__(self, position: int = 0, player: Player = NullPlayer()) -> None:
        self.__position = position
        self.__player = player

    @property
    def position(self) -> int:
        return self.__position

    @property
    def player(self) -> Player:
        return self.__player

    @player.setter
    def player(self, player: Player) -> None:
        self.__player = player

    def is_owned(self) -> bool:
        """ Returns whether this cell is owned by a player.
        :return: "False" if the player within this cell is an instance of `NullPlayer`. Else "True".
        """
        return not isinstance(self.player, NullPlayer)

    def __str__(self) -> str:
        return self.player.marker.character \
            if self.player.marker.character != NullPlayer().marker.character \
            else str(self.position + 1)


class NullCell(Cell):

    def __init__(self) -> None:
        super().__init__(-1, NullPlayer())

    @property
    def position(self) -> int:
        return super().position

    @property
    def player(self) -> Player:
        return super().player

    @player.setter
    def player(self, player: Player) -> None:
        pass

    def is_owned(self) -> bool:
        return super().is_owned()

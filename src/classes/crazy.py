from random import randint

from .player import Player
from .tictactoe import TicTacToe


class Crazy(TicTacToe):

    def __init__(self) -> None:
        self.__random_counter = 1
        super().__init__()

    @staticmethod
    def name() -> str:
        return "Crazy"

    @property
    def random_counter(self) -> int:
        """ Indicates for how many times the current player has been selected randomly.
        :return: Integer, telling for how many times the current player has been selected randomly.
        """
        return self.__random_counter

    @random_counter.setter
    def random_counter(self, random_counter: int) -> None:
        self.__random_counter = random_counter

    def choose_random_player(self) -> None:
        random_player_id: int = randint(0, len(self.players) - 1)
        next_random_player: Player = self.players[random_player_id]
        current_player: Player = self.players[self.current_player]

        if next_random_player == current_player:

            # Switch to next player if current player was chosen randomly twice
            if self.random_counter >= 2:
                super().switch_player()

            self.random_counter += 1
            return

        # Reset counter and choose random player
        self.random_counter = 1
        self.current_player = random_player_id

    def switch_player(self) -> None:
        self.choose_random_player()

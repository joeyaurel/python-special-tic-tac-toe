from .gametype import GameType
from .player import Player


class TicTacToe(GameType):

    @staticmethod
    def name() -> str:
        return "Tic Tac Toe"

    def mark_cell(self, position: int, player: Player) -> bool:
        if position in self.board.cells:
            self.board.cells[position].player = player
            return True

        return False

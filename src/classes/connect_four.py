from .gametype import GameType
from .player import Player


class ConnectFour(GameType):

    @staticmethod
    def name() -> str:
        return "Connect Four"

    def mark_cell(self, position: int, player: Player) -> bool:

        if not self.board.cell_exists(position):
            return False

        cell_position_below = position + self.board.size

        # Only allow the player to place a cell if the cell below
        # does not exist or is owned by a player
        if not self.board.cell_exists(cell_position_below) \
                or self.board.cell(cell_position_below).is_owned():
            self.board.cells[position].player = player
            return True

        return False

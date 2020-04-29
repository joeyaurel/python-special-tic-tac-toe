from collections import OrderedDict
from math import floor
from random import randint

from .board import Board
from .cell import Cell
from .helpers import integer_input, clear_output
from .marker import Marker
from .player import Player


class GameType:

    def __init__(self) -> None:
        self.__board: Board = Board()
        self.__players: list = list()
        self.__current_player: int = 0
        self.__cells_to_win: int = self.board.size
        self.__won_cells: list = list()
        self.__in_game: bool = False

    @staticmethod
    def name() -> str:
        """ The name of this game type. """
        return ""

    @property
    def board(self) -> Board:
        return self.__board

    @property
    def players(self) -> list:
        return self.__players

    @players.setter
    def players(self, players: list) -> None:
        # Do not change players while in game
        if self.is_in_game:
            return

        self.__players = players

    @property
    def current_player(self) -> int:
        return self.__current_player

    @current_player.setter
    def current_player(self, current_player: int) -> None:
        self.__current_player = current_player if 0 <= current_player < len(self.players) else 0

    @property
    def cells_to_win(self) -> int:
        return self.__cells_to_win

    @cells_to_win.setter
    def cells_to_win(self, cells_to_win: int) -> None:
        self.__cells_to_win = cells_to_win

    @property
    def won_cells(self) -> list:
        return self.__won_cells

    @won_cells.setter
    def won_cells(self, won_cells: list) -> None:
        self.__won_cells = won_cells

    @property
    def is_in_game(self) -> bool:
        return self.__in_game

    def choose_random_player(self) -> None:
        self.__current_player = randint(0, len(self.players) - 1)

    def switch_player(self) -> None:
        if self.current_player < len(self.players) - 1:
            self.__current_player += 1
            return

        self.__current_player = 0

    def determine_won_cell_positions(self, position: int, marker: Marker) -> list:
        """ Determines all cells whose markers are equal to the provided marker "beginning" at the given `position`.

        Depending on the game type, this method may check cells horizontally, vertically, diagonally from left
        to right and diagonally from right to left.

        This method returns a list containing the positions of the cells that won if there are any cells that won.

        :param int position: The position of the cell to check.
        :param Marker marker: The marker that should equal to the cells that won.
        :return: A list containing the positions of the cells that won, if there are any cells that won.
                 Else an empty list.
        """
        won_cells: list = list()

        won_cells.extend(self.__determine_won_cells_horizontally(position, marker))
        won_cells.extend(self.__determine_won_cells_vertically(position, marker))
        won_cells.extend(self.__determine_won_cells_diagonally_left_to_right(position, marker))
        won_cells.extend(self.__determine_won_cells_diagonally_right_to_left(position, marker))

        return won_cells

    def __determine_won_cells_horizontally(self, position: int, marker: Marker) -> list:
        column: float = position % self.board.size

        # Get the minimum horizontal position from where to start
        from_position: float = position - column

        # Get the maximum horizontal position where to stop
        to_position: float = position + ((self.board.size - 1) - column)

        return self.__filter_won_cell_positions(
            self.__determine_checking_range(int(from_position), int(to_position), 1),
            marker
        )

    def __determine_won_cells_vertically(self, position: int, marker: Marker) -> list:
        row: float = floor(position / self.board.size)

        # Get the minimum vertical position from where to start
        from_position: float = position - (row * self.board.size)

        # Get the maximum vertical position where to stop
        to_position: float = position + ((self.board.size - row) - 1) * self.board.size

        return self.__filter_won_cell_positions(
            self.__determine_checking_range(int(from_position), int(to_position), self.board.size),
            marker
        )

    def __determine_won_cells_diagonally_left_to_right(self, position: int, marker: Marker) -> list:
        row: float = floor(position / self.board.size)
        column: float = position % self.board.size

        # Get the minimum diagonal position beginning in the top left
        from_position: float = position - min(row, column) * (self.board.size + 1)

        # Get the maximum diagonal position stopping in the bottom right
        to_position: float = position + (self.board.size - max(row, column) - 1) * (self.board.size + 1)

        return self.__filter_won_cell_positions(
            self.__determine_checking_range(int(from_position), int(to_position), self.board.size + 1),
            marker
        )

    def __determine_won_cells_diagonally_right_to_left(self, position: int, marker: Marker) -> list:
        row: float = floor(position / self.board.size)
        column: float = position % self.board.size

        # Get the minimum diagonal position beginning in the bottom left
        from_position: float = position - min(row, (self.board.size - column) - 1) * (self.board.size - 1)

        # Get the maximum diagonal position stopping in the top right
        to_position: float = position + (self.board.size - max(row + 1, self.board.size - column)) * (
                self.board.size - 1)

        return self.__filter_won_cell_positions(
            self.__determine_checking_range(int(from_position), int(to_position), self.board.size - 1),
            marker
        )

    @staticmethod
    def __determine_checking_range(from_position: int, to_position: int, step_size: int) -> list:
        return list(set(range(
            from_position,
            to_position + 1,
            step_size
        )))

    def __filter_won_cell_positions(self, cell_positions: list, marker: Marker) -> list:

        cells_to_check: dict = dict()
        won_cells: list = list()

        # Go though indexes and find relevant cells to check
        for cell_position in cell_positions:

            # Check if cell by `index` actually exists and wasn't already added to `cells`
            if cell_position not in self.board.cells or cell_position in cells_to_check:
                continue

            cells_to_check[cell_position] = self.board.cells[cell_position]

        # Sort `cells_to_check` by their cell position with `OrderedDict`
        ordered_cells_to_check: dict = OrderedDict(
            sorted(cells_to_check.items())
        )

        for cell_position, cell in ordered_cells_to_check.items():

            # Add the current cell if no won cells exist yet and if
            # its marker equals the marker we provided
            if len(won_cells) == 0:

                if cell.player.marker == marker:
                    won_cells.append(cell)

                continue

            # Get the last won cell
            last_won_cell: Cell = won_cells[-1]

            # Check if the marker of the last inserted cell equals the marker
            # of the current cell and the provided marker
            if last_won_cell.player.marker == cell.player.marker == marker:
                won_cells.append(cell)
                continue

            # If there are enough cells to satisfy a winning situation break the loop
            if len(won_cells) >= self.cells_to_win:
                break

            # If none of the above conditions were met, reset `won_cells`
            won_cells = list()

        # Only return the list of positions of won cells if there are enough won cells to satisfy a winning situation.
        # If this condition is not satisfied return an empty `list`.
        return [won_cell.position for won_cell in won_cells] if len(won_cells) >= self.cells_to_win else list()

    def print_board(self, won_cells: list = list()) -> None:
        clear_output()
        print(self.board.format_board(won_cells))

    def start_new_game(self) -> None:
        self.reset_board_cells()
        self.choose_random_player()
        self.play()

    def reset_board_cells(self) -> None:
        """Removes all cells and adds fresh new cells depending on the current board size.

        May be useful after a board resize (`size` lowered or raised) or if you
        just want to reset all cells within this board.
        """
        square: int = self.board.size ** 2
        self.board.cells = {position: Cell(position) for position in range(square)}

    def mark_cell(self, position: int, player: Player) -> bool:
        """ Place a placer at the given cell position.
        :param int position: The cell position.
        :param Player player:  The placer to be set.
        :return: "True" if the player was successfully set. Else "False".
        """
        pass

    def play(self) -> None:

        # Change state of game
        self.__in_game = True

        self.print_board()

        player: Player = self.players[self.current_player]

        print("It's your turn, \033[{}m{}\033[0m! (Marker: {})".format(
            player.color,
            player.name,
            player.marker.character)
        )

        correct_input: bool = False

        while correct_input is False:

            position = integer_input("Type in your position (number): ") - 1

            if not self.mark_cell(position, player):
                print("Could not mark this cell. Please take another one.")
                continue

            correct_input = True

            won_cells: list = self.determine_won_cell_positions(position, player.marker)

            if self.board.is_full():
                self.__in_game = False
                self.print_board()
                print('Draw!')
                return

            if len(won_cells) > 0:
                self.__in_game = False
                self.print_board(won_cells)
                return

        self.switch_player()
        self.play()


class NullGameType(GameType):

    def __init__(self) -> None:
        super().__init__()

    @property
    def board(self) -> Board:
        return super().board

    @property
    def players(self) -> list:
        return super().players

    @players.setter
    def players(self, players: list) -> None:
        pass

    @property
    def current_player(self) -> int:
        return super().current_player

    @current_player.setter
    def current_player(self, current_player: int) -> None:
        pass

    @property
    def cells_to_win(self) -> int:
        return super().cells_to_win

    @cells_to_win.setter
    def cells_to_win(self, cells_to_win: int) -> None:
        pass

    @property
    def is_in_game(self) -> bool:
        return super().is_in_game

    def choose_random_player(self) -> None:
        pass

    def switch_player(self) -> None:
        pass

    def determine_won_cell_positions(self, position: int, marker: Marker) -> list:
        pass

    def print_board(self, won_cells: list = list()) -> None:
        pass

    def start_new_game(self) -> None:
        pass

    def reset_board_cells(self) -> None:
        pass

    def mark_cell(self, position: int, player: Player) -> bool:
        pass

    def play(self) -> None:
        pass

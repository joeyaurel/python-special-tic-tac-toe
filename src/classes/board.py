from .cell import Cell, NullCell
from .colors import ASCII_COLOR_GREEN
from .marker import NullMarker
from .player import NullPlayer


class Board:

    def __init__(self, size: int = 3) -> None:
        # Force board to have a minimum size of three cells per row
        self.__size = size if size >= 3 else 3
        self.__cells = dict()

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
        """Set the current size of the board. This method forces the given `size` to be greater or equal to `3`.
        :type size: int
        """
        self.__size = size if size >= 3 else 3

    @property
    def cells(self) -> dict:
        return self.__cells

    @cells.setter
    def cells(self, cells: dict) -> None:
        self.__cells = cells

    def cell(self, position: int) -> Cell:
        """Get one `Cell` by its `position`, if it exists, else a `NullCell`.
        :type position: inn
        """
        return self.cells[position] if self.cell_exists(position) else NullCell()

    def cell_exists(self, position: int) -> bool:
        return position in self.cells

    def cell_taken(self, position: int) -> bool:
        return self.cell_exists(position) and not isinstance(self.cells[position].player.marker, NullMarker)

    def is_full(self) -> bool:
        taken_cells = [
            cell
            for index, cell in self.cells.items()
            if not isinstance(cell.player, NullPlayer)
        ]

        return len(taken_cells) == self.size ** 2

    def format_board(self, won_cells: list = None) -> str:
        """ Formats this board into a printable format.
        :rtype: str
        """
        if won_cells is None:
            won_cells = list()

        board_output: str = '\n\n'

        # Define separators used to separate cell values
        value_separator: str = ' | '
        line_separator: str = '-'

        # The padding sets space for available cell values, calculated
        # by the length of the largest cell position available.
        cell_space: int = len(str(self.size ** 2))

        # Calculate how many characters will be printed for each line
        # to later tell how many line separators for a line have to
        # be printed.
        total_cell_space: int = (cell_space * self.size)
        total_value_separator_characters: int = len(
            value_separator) * self.size - 1
        total_line_characters: int = total_cell_space + \
            total_value_separator_characters - 2

        for index, cell in self.cells.items():

            # Print a line separator before each line but not the first.
            # `(index + 1) % BOARD_SIZE` equals `1` if it is a new line.
            if cell.position > 0 and (cell.position + 1) % self.size is 1:
                board_output += '\n' + line_separator * total_line_characters + '\n'

            cell_value_with_padding: str = str(cell).ljust(cell_space)

            if cell.position in won_cells:
                board_output += '\033[{}m{}\033[0m'.format(
                    ASCII_COLOR_GREEN, cell_value_with_padding)
            elif isinstance(cell.player.marker, NullMarker) or self.is_full():
                board_output += cell_value_with_padding
            else:
                board_output += '\033[{}m{}\033[0m'.format(
                    cell.player.color, cell_value_with_padding)

            # Separate the values by `value_separator`
            if (cell.position + 1) % self.size > 0:
                board_output += value_separator

        board_output += '\n\n'

        return board_output

    def __str__(self) -> str:
        return self.format_board()

from random import randint

from .connect_four import ConnectFour
from .crazy import Crazy
from .gametype import GameType, NullGameType
from .helpers import choose_random_player_color, integer_input
from .marker import Marker
from .player import Player
from .tictactoe import TicTacToe


class GameBuilder:

    def __init__(self):
        self.available_game_types = {
            0: TicTacToe,
            1: ConnectFour,
            2: Crazy,
        }

    def build(self) -> GameType:
        chosen_game_type: GameType = self.__choose_game_type()
        print('Chosen game type: {}'.format(chosen_game_type.name()))

        number_of_players: int = self.__choose_number_of_players()

        chosen_game_type.board.size = integer_input('Board size: ')
        chosen_game_type.cells_to_win = integer_input('Number of cells to win the game: ')

        chosen_game_type.reset_board_cells()

        players = list()

        for player_id in range(0, number_of_players):
            players.append(Player(
                input('Name of player {}: '.format(player_id + 1)),
                Marker(input('Marker of player {}: '.format(player_id + 1))),
                choose_random_player_color(players)
            ))

        chosen_game_type.players = players

        return chosen_game_type

    def __choose_game_type(self) -> GameType:
        chosen_game_type: GameType = NullGameType()

        while isinstance(chosen_game_type, NullGameType):

            chosen_game_type_id = integer_input(
                'Game type (0: Random, {}): '.format(', '.join([
                    "{}: {}".format(game_type_id + 1, game_type.name())
                    for game_type_id, game_type
                    in self.available_game_types.items()
                ]))
            )

            if chosen_game_type_id == 0:
                # Choose random game type
                chosen_game_type = self.available_game_types[randint(0, len(self.available_game_types) - 1)]()
            elif chosen_game_type_id - 1 in self.available_game_types:
                # Create a new instance of the chosen game type
                chosen_game_type = self.available_game_types[chosen_game_type_id - 1]()
            else:
                print('Wrong game type.')

        return chosen_game_type

    def __choose_number_of_players(self) -> int:
        number_of_players = 0

        while number_of_players is 0:

            chosen_number_of_players = integer_input('Number of players: ')

            if chosen_number_of_players < 2:
                print('There must be a minimum of two players.')
            elif chosen_number_of_players > 5:
                print('There is a maximum of five players.')
            else:
                number_of_players = chosen_number_of_players

        return number_of_players

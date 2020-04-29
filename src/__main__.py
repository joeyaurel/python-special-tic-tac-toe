from classes.game_builder import GameBuilder
from classes.gametype import GameType

if __name__ == "__main__":
    game_builder = GameBuilder()
    game_type: GameType = game_builder.build()
    game_type.start_new_game()

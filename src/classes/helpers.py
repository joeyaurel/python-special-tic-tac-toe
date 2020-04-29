from .colors import random_ascii_color_but_not_in, random_ascii_color


def clear_output() -> None:
    print('\n' * 120)


def integer_input(message='') -> int:
    number = input(message)

    # Try to convert input to an integer. Raise an error if it could not be converted.
    # In other words the input does not represent a valid number.
    try:
        number = int(number)
    except ValueError:
        pass  # do job to handle: s does not contain anything convertible to int
    except Exception:
        pass  # do job to handle: Exception occurred while converting to int

    return number if isinstance(number, int) else 0


def choose_random_player_color(players: list) -> str:
    if len(players) == 0:
        return random_ascii_color()

    colors: list = [player.color for player in players]
    color: str = random_ascii_color_but_not_in(colors)

    return color

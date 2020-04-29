from random import randint

ASCII_COLOR_RESET: str = "00"
ASCII_COLOR_BLACK: str = "0;30"
ASCII_COLOR_RED: str = "0;31"
ASCII_COLOR_GREEN: str = "0;32"
ASCII_COLOR_YELLOW: str = "0;33"
ASCII_COLOR_BLUE: str = "0;34"
ASCII_COLOR_PURPLE: str = "0;35"
ASCII_COLOR_CYAN: str = "0;36"
ASCII_COLOR_LIGHT_GRAY: str = "0;37"
ASCII_COLOR_DARK_GRAY: str = "1;30"
ASCII_COLOR_BOLD_RED: str = "1;31"
ASCII_COLOR_BOLD_GREEN: str = "1;32"
ASCII_COLOR_BOLD_YELLOW: str = "1;33"
ASCII_COLOR_BOLD_BLUE: str = "1;34"
ASCII_COLOR_BOLD_PURPLE: str = "1;35"
ASCII_COLOR_BOLD_CYAN: str = "1;36"
ASCII_COLOR_WHITE: str = "1;37"


def random_ascii_color() -> str:
    colors: list = [
        # ASCII_COLOR_BLACK,
        ASCII_COLOR_RED,
        # ASCII_COLOR_GREEN,  # Taken by won cells
        ASCII_COLOR_YELLOW,
        ASCII_COLOR_BLUE,
        ASCII_COLOR_PURPLE,
        ASCII_COLOR_CYAN,
        # ASCII_COLOR_LIGHT_GRAY,
        # ASCII_COLOR_DARK_GRAY,
        # ASCII_COLOR_BOLD_RED,
        # ASCII_COLOR_BOLD_GREEN,
        # ASCII_COLOR_BOLD_YELLOW,
        # ASCII_COLOR_BOLD_BLUE,
        # ASCII_COLOR_BOLD_PURPLE,
        # ASCII_COLOR_BOLD_CYAN,
        # ASCII_COLOR_WHITE,
    ]

    random_number: int = randint(0, len(colors) - 1)
    return colors[random_number]


def random_ascii_color_but_not(color: str) -> str:
    found_color = color

    while found_color == color:
        found_color = random_ascii_color()

    return found_color


def random_ascii_color_but_not_in(colors: list) -> str:
    random_color = random_ascii_color()

    while random_color in colors:
        random_color = random_ascii_color()

    return random_color

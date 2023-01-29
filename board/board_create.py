from board.board_const import WALL, EMPTY_COORDINATES, EMPTY_SPACE


def create_board(file):
    """
    Creates a new game board based on input parameters.
    Args:
    int: The width of the board
    int: The height of the board
    Returns:
    list: Game board
    """
    width = 40
    height = 20
    board = [[" " for _ in range(width)] for _ in range(height)]

    return board


def create_board_from_file(file):
    with open(file) as file:
        lines = file.readlines()
        lines = [list(line.strip()) for line in lines]
        return lines
    
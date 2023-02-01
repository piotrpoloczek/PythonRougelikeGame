from board.board_const import WALL, EMPTY_COORDINATES, EMPTY_SPACE


def create_empty_board(file):
    width = 40
    height = 20
    return [[" " for _ in range(width)] for _ in range(height)]

def create_board_from_file(file):
    with open(file) as file:
        lines = file.readlines()
        lines = [list(line.strip()) for line in lines]
        return lines
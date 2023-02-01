from exception.exception_custom import CoordinateException
from entities.coordinates.coordinates_get import get_x_y_coordinates
from entities.entities_get import get_coordinates, get_symbol
from board.board_const import EMPTY_COORDINATES


def set_character_on_board(board, player):
    try:
        coordinates_list = get_coordinates(player)
        for coordinates in coordinates_list:
            x, y = get_x_y_coordinates(coordinates)
            board[y][x] = get_symbol(player)
    except Exception as e:
        print(e)

def set_empty_coordinates_on_board(board, coordinates_list):
    for coordinates in coordinates_list:
        x, y = get_x_y_coordinates(coordinates)
        board[y][x] = EMPTY_COORDINATES
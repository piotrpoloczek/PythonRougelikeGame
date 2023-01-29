from exception.exception_custom import CoordinateException
from coordinates.coordinates_get import get_x_y_coordinates
from character.character_get import get_coordinates


def set_character_on_board(board, player):
    try:
        coordinates_list = get_coordinates(player)
        for coordinates in coordinates_list:
            x, y = get_x_y_coordinates(coordinates)
            board[y][x] = player["icon"]
    except Exception as e:
        print(e)

def set_empty_coordinates_on_board(board, coordinates_list):
    for coordinates in coordinates_list:
        x, y = get_x_y_coordinates(coordinates)
        board[y][x] = '-'
from exception.exception_custom import CoordinateException
from board.board_get import get_board_available_coordiantes, get_board_character_coordinates


def check_new_coordinates(coordiantes_list, board, character):
    available_coordiantes = get_board_available_coordiantes(board)
    character_coordinates = get_board_character_coordinates(board, character)
    for coordinates in coordiantes_list:
        if coordinates not in available_coordiantes and coordinates not in character_coordinates:
            raise CoordinateException
    return True
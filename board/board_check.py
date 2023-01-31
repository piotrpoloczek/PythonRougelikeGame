from exception.exception_custom import CoordinateException, ItemFoundException
from board.board_get import get_board_available_coordiantes, get_board_character_coordinates
from items.items_get import get_board_items_coordiantes, get_items_from_board


def check_new_coordinates(coordiantes_list, board, character):
    available_coordiantes = get_board_available_coordiantes(board)
    character_coordinates = get_board_character_coordinates(board, character)
    item_coordinates = get_board_items_coordiantes(board)
    print('item_coordiantres: ', item_coordinates)
    print('coordiantes_list : ', coordiantes_list)
    for coordinates in coordiantes_list:
        if coordinates in item_coordinates:
            raise ItemFoundException(coordinates)
        if coordinates not in available_coordiantes and coordinates not in character_coordinates:
            raise CoordinateException
    return True
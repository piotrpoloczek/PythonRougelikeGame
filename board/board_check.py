from exception.exception_custom import CoordinateException, ItemFoundException, FightException
from board.board_get import get_board_available_coordiantes, get_board_character_coordinates
from items.items_get import get_board_items_coordiantes, get_items_from_board
from game.game_get import get_board_opponents_items
from character.opponent.opponent_get import get_coordiantes_with_opponents, remove_symbol


def check_new_coordinates(coordiantes_list, character, level):
    board, opponents, items = get_board_opponents_items(level)
    available_coordiantes = get_board_available_coordiantes(board)
    character_coordinates = get_board_character_coordinates(board, character)
    item_coordinates = get_board_items_coordiantes(board)
    opponents_coordinates = remove_symbol(get_coordiantes_with_opponents(board))
    print('opponents coordinates list: ', opponents_coordinates)
    print('item_coordiantres: ', item_coordinates)
    print('coordiantes_list : ', coordiantes_list)
    for coordinates in coordiantes_list:
        if coordinates in opponents_coordinates:
            raise FightException
        elif coordinates in item_coordinates:
            raise ItemFoundException(coordinates)
        elif coordinates not in available_coordiantes and coordinates not in character_coordinates:
            raise CoordinateException
    return True
from exception.exception_custom import CoordinateException, ItemFoundException, FightException, ExitException
from board.board_get import get_board_available_coordiantes, get_board_character_coordinates, get_exit_coordinates
from level.level_get import get_board_opponents_items_characters
from entities.entities_get_all import get_list_coordiantes_from_entities, get_entity_by_coordinates
from entities.entities_get import get_coordinates


def check_new_coordinates(coordiantes_list, character, level):
    board, opponents, items, characters = get_board_opponents_items_characters(level)

    available_coordiantes = get_board_available_coordiantes(board)
    character_coordinates = get_board_character_coordinates(board, character)
    item_coordinates = get_list_coordiantes_from_entities(items)
    opponents_coordinates = get_list_coordiantes_from_entities(opponents)
    characters_coordinates = get_list_coordiantes_from_entities(characters)

    print('coordiantes_list : ', coordiantes_list)
    print('opponents coordinates list: ', opponents_coordinates)
    print('items coordinaes_list: ', item_coordinates)


    for coordinates in coordiantes_list:
        if check_coordinate_in_opponents(coordinates, opponents) and coordinates not in character_coordinates:
            opponent = get_entity_by_coordinates(opponents, [coordinates])
            raise FightException(opponent)
        elif check_coordinate_in_items(coordinates, items):
            item = get_entity_by_coordinates(items, [coordinates])
            raise ItemFoundException(item)
        elif coordinates in get_exit_coordinates(board):
            raise ExitException
        elif coordinates not in available_coordiantes and coordinates not in character_coordinates:
            raise CoordinateException
    return True

def check_coordinate_in_items(x_y_coordinates, items):
    return check_coordinates_in_objects(x_y_coordinates, items)

def check_coordinate_in_opponents(x_y_coordinates, opponents):
    return check_coordinates_in_objects(x_y_coordinates, opponents)

def check_coordinates_in_objects(x_y_coordinates, objects):
    for object in objects:
        if x_y_coordinates in get_coordinates(object):
            return True
    return False


    
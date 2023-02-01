from copy import deepcopy
from board.board_get import get_board_coordiantes_symbols
from entities.entities_get_all import get_entity_by_symbol, get_list_symbols_from_entities
from entities.entities_get import get_symbol
from entities.coordinates.coordinates_get import get_x_y_coordinates
from entities.coordinates.coordinates_create import create_coordinates
from entities.entities_set import set_coordinates


def get_coordiantes_with_entities(board, entities_list):
    items_coordinates = []
    coordinates = get_board_coordiantes_symbols(board)
    symbols = get_list_symbols_from_entities(entities_list)
    for coordinate in coordinates:
        if get_symbol(coordinate) in symbols:
            items_coordinates.append(coordinate)
    return items_coordinates

def get_entities_from_board(board, entities_list):
    entities = []
    entities_coordinates = get_coordiantes_with_entities(board, entities_list)
    for entity_coordinates in entities_coordinates:
        symbol = get_symbol(entity_coordinates)
        entity = deepcopy(get_entity_by_symbol(entities_list, symbol))
        x_coordinate, y_coordinate = get_x_y_coordinates(entity_coordinates)
        coordinates_list = [create_coordinates(x_coordinate, y_coordinate)]
        set_coordinates(entity, coordinates_list)
        entities.append(entity)
        #print('entities :', entities)
    return entities
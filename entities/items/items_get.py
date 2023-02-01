from copy import deepcopy
from entities.entities_const import NAME, SYMBOL, COORDINATES
from entities.items.items_const import TYPE, QUANTITY, POWER
from entities.items.items_list import ITEMS
from exception.exception_custom import ItemNotFoundException
from board.board_get import get_board_coordiante, get_board_coordiantes_symbol
from entities.items.items_set import set_coordinates
from entities.coordinates.coordinates_get import get_x_y_coordinates
from entities.coordinates.coordinates_create import create_coordinates


def get_type(item):
    return item[TYPE]

def get_name(item):
    return item[NAME]

def get_quantity(item):
    return item[QUANTITY]

def get_power(item):
    return item[POWER]

def get_symbol(item):
    return item[SYMBOL]

def get_item_coordinates(item):
    return item[COORDINATES]

def get_item_by_symbol(symbol):
    for item in ITEMS:
        if get_symbol(item) == symbol:
            return item

def get_item_by_coordiantes(items, coordinates):
    for item in items:
        if get_item_coordinates(item) == coordinates[0]:
            return item

def get_all_symbols():
    symbols = []
    for item in ITEMS:
        symbols.append(get_symbol(item))
    return symbols

def get_board_items_coordiantes(board):
    items = get_items_from_board(board)
    items_coordinates = []
    for item in items:
        items_coordinates.append(get_item_coordinates(item))
    return items_coordinates

def get_coordiantes_with_items(board):
    items_coordinates = []
    coordinates = get_board_coordiantes_symbol(board)
    symbols = get_all_symbols()
    for coordinate in coordinates:
        if get_symbol(coordinate) in symbols:
            items_coordinates.append(coordinate)
    return items_coordinates


def get_items_from_board(board):
    opponents = []
    opponents_coordinates = get_coordiantes_with_items(board)
    for opponent_coordinates in opponents_coordinates:
        opponent = deepcopy(get_item_by_symbol(get_symbol(opponent_coordinates)))
        x_coordinate, y_coordinate = get_x_y_coordinates(opponent_coordinates)
        coordinates_list = [create_coordinates(x_coordinate, y_coordinate)]
        set_coordinates(opponent, coordinates_list)
        opponents.append(opponent)
    return opponents
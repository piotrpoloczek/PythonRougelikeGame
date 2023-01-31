from items.items_const import TYPE, NAME, QUANTITY, POWER, SYMBOL, COORDINATES
from items.items_list import ITEMS
from exception.exception_custom import ItemNotFoundException
from board.board_get import get_board_coordiante
from items.items_set import set_coordinates


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

def get_items_from_board(board):
    items = []
    symbols = get_all_symbols()
    for symbol in symbols:
        item_coordinates = get_board_coordiante(board, symbol)
        item = get_item_by_symbol(symbol)
        set_coordinates(item, item_coordinates)
        items.append(item)
    return(items)

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

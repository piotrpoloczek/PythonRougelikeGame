from items.items_const import TYPE, NAME, QUANTITY, POWER, SYMBOL, COORDINATES
from exception.exception_custom import ItemNotFoundException


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

def get_coordinates(item):
    return item[COORDINATES]

def get_item_from_items(coordinates):
    items = get_items_list()
    for item in items:
        if get_coordinates(item) == coordinates:
            return item
    raise ItemNotFoundException

def get_items_list(board):
    pass

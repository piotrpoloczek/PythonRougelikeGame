from entities.items.items_const import TYPE, QUANTITY, POWER
from entities.items.items_list import ITEMS
from entities.entities_get_from_board import get_entities_from_board


def get_type(item):
    return item[TYPE]

def get_quantity(item):
    return item[QUANTITY]

def get_power(item):
    return item[POWER]

def get_items_from_board(board):
    return get_entities_from_board(board, ITEMS)


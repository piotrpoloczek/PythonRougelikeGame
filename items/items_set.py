from items.items_const import TYPE, NAME, QUANTITY, POWER, SYMBOL, COORDINATES
from coordinates.coordinates_create import create_coordinates_list_one_coordinate


def set_type(item, type):
    item[TYPE] = type

def set_name(item, name):
    item[NAME] = name

def set_quantity(item, quantity):
    item[QUANTITY] = quantity

def set_power(item, power):
    item[POWER] = power

def set_symbol(item, symbol):
    item[SYMBOL] = symbol

def set_coordinates(item, coordinates):
    item[COORDINATES] = coordinates


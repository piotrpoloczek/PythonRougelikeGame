from entities.entities_const import NAME, SYMBOL, COORDINATES, TYPE


def set_name(entity, name):
    entity[NAME] = name

def set_symbol(entity, symbol):
    entity[SYMBOL] = symbol

def set_coordinates(entity, coordinates):
    entity[COORDINATES] = coordinates

def set_type(entity, type):
    entity[TYPE] = type